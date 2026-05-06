/**
 * GoatCounter stats proxy — Cloudflare Worker
 *
 * Why this exists:
 *   GoatCounter API는 인증 필요 (Bearer token). 토큰을 클라이언트 JS에 두면 노출.
 *   Worker가 토큰을 환경변수로 보관하고, 브라우저는 Worker URL만 호출 → 토큰 격리.
 *
 * Required env vars (set via Cloudflare dashboard or wrangler):
 *   GOATCOUNTER_SITE   — your goatcounter site code (예: "joyuno")
 *   GOATCOUNTER_TOKEN  — API token from goatcounter.com → settings → API
 *
 * Optional:
 *   ALLOWED_ORIGIN     — CORS origin (기본: https://joyuno.github.io)
 *
 * Endpoint: GET /  →  {today, week, total, generated_at}
 *
 * Caching: 응답을 5분간 CDN edge에 캐싱 → 페이지뷰 폭발해도 GoatCounter 호출은 분당 ≤1회.
 */

const CACHE_TTL_SECONDS = 300; // 5min

export default {
  async fetch(request, env, ctx) {
    const allowedOrigin = env.ALLOWED_ORIGIN || "https://joyuno.github.io";

    // CORS preflight
    if (request.method === "OPTIONS") {
      return corsResponse(allowedOrigin);
    }
    if (request.method !== "GET") {
      return json({ error: "method not allowed" }, 405, allowedOrigin);
    }

    // 캐시 조회
    const cacheKey = new Request(new URL(request.url).toString(), { method: "GET" });
    const cache = caches.default;
    const cached = await cache.match(cacheKey);
    if (cached) {
      // 헤더에 X-Cache-Hit 표시
      const r = new Response(cached.body, cached);
      r.headers.set("X-Cache-Hit", "1");
      return r;
    }

    if (!env.GOATCOUNTER_SITE || !env.GOATCOUNTER_TOKEN) {
      return json({ error: "worker missing GOATCOUNTER_SITE / GOATCOUNTER_TOKEN" }, 500, allowedOrigin);
    }

    const base = `https://${env.GOATCOUNTER_SITE}.goatcounter.com/api/v0`;
    const headers = {
      "Authorization": `Bearer ${env.GOATCOUNTER_TOKEN}`,
      "Content-Type": "application/json",
    };

    const todayStart = isoDate(new Date()) + "T00:00:00Z";
    const weekStart = isoDate(daysAgo(7)) + "T00:00:00Z";

    try {
      const [todayRes, weekRes, totalRes] = await Promise.all([
        fetchTotal(base, headers, todayStart),
        fetchTotal(base, headers, weekStart),
        fetchTotal(base, headers, null),
      ]);

      const body = {
        today: todayRes,
        week: weekRes,
        total: totalRes,
        generated_at: new Date().toISOString(),
      };

      const response = json(body, 200, allowedOrigin, CACHE_TTL_SECONDS);
      // 백그라운드에 캐시 저장 (응답 차단 안 함)
      ctx.waitUntil(cache.put(cacheKey, response.clone()));
      return response;
    } catch (e) {
      return json({ error: String(e).slice(0, 200) }, 502, allowedOrigin);
    }
  },
};

async function fetchTotal(base, headers, startIso) {
  const url = startIso
    ? `${base}/stats/total?start=${encodeURIComponent(startIso)}`
    : `${base}/stats/total`;
  const r = await fetch(url, { headers });
  if (!r.ok) throw new Error(`goatcounter ${r.status}: ${await r.text().then(t => t.slice(0, 100))}`);
  const j = await r.json();
  // GoatCounter 응답 모양: {total: <number>, ...}
  return Number(j.total ?? j.count ?? 0);
}

function isoDate(d) {
  return d.toISOString().split("T")[0];
}

function daysAgo(n) {
  return new Date(Date.now() - n * 86400 * 1000);
}

function corsResponse(origin) {
  return new Response(null, {
    status: 204,
    headers: {
      "Access-Control-Allow-Origin": origin,
      "Access-Control-Allow-Methods": "GET, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type",
      "Access-Control-Max-Age": "86400",
    },
  });
}

function json(obj, status, origin, sMaxAge) {
  const headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Access-Control-Allow-Origin": origin,
  };
  if (sMaxAge) {
    headers["Cache-Control"] = `public, s-maxage=${sMaxAge}`;
  }
  return new Response(JSON.stringify(obj), { status, headers });
}
