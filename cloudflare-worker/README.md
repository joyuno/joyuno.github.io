# Views Proxy — Cloudflare Worker

GoatCounter API 토큰을 격리하기 위한 thin proxy.

## 셋업 (1회, 약 15분)

### 1. GoatCounter 계정 생성
1. https://www.goatcounter.com/signup 가입 (무료, 개인 사이트 OK)
2. 사이트 코드 정하기 (예: `joyuno` → 대시보드 URL = `joyuno.goatcounter.com`)
3. 사이트 추가 → URL = `https://joyuno.github.io`
4. **Settings → API** → "Create new token" → 권한은 `count` + `read site` 만 체크 → 토큰 복사

### 2. Cloudflare 계정 + Worker 배포

```bash
# wrangler 설치 (한 번)
npm install -g wrangler

# 로그인
wrangler login

cd cloudflare-worker

# 시크릿 등록 (대화형)
wrangler secret put GOATCOUNTER_SITE
# → 입력: joyuno  (위에서 정한 사이트 코드)

wrangler secret put GOATCOUNTER_TOKEN
# → 입력: gc-... (위에서 복사한 토큰)

# 배포
wrangler deploy
```

배포 끝나면 콘솔에 URL이 찍힙니다 (예: `https://joyuno-views-proxy.<your-handle>.workers.dev`).

### 3. 블로그에 Worker URL 박기

`_layouts/default.html` 의 `VIEWS_PROXY_URL` 상수를 위 URL로 교체.

## 동작 확인

```bash
curl -s https://joyuno-views-proxy.<your-handle>.workers.dev | jq
# → {"today": 12, "week": 89, "total": 1234, "generated_at": "..."}
```

응답이 `5분간 edge cache`에 저장되므로 트래픽이 늘어도 GoatCounter API는 분당 1회 이하만 호출됩니다.

## 비용

- GoatCounter: 개인 사이트 무료
- Cloudflare Workers: 100k req/day 무료 (개인 블로그는 사실상 무료)

## 시크릿이 새지 않는다는 보장

- 토큰은 Cloudflare Worker 환경변수에만 저장 — 코드/저장소에 절대 박지 않음
- 브라우저는 Worker URL만 호출 → 응답은 합산된 숫자만 반환
- 만에 하나 토큰이 유출돼도 GoatCounter 권한은 `read site / count` 만이라 데이터 추가/삭제 불가
