/* 회전하는 OIIA 고양이 파비콘 — canvas 로 매 프레임 favicon URL 갱신.
   Chrome/Safari 는 GIF/SVG 애니메이션 favicon 을 native 지원 안 함 → JS swap 이 유일.

   사용:
     window.faviconSpinner.start()  // 회전 시작 (예: 데이터 로드 시작)
     window.faviconSpinner.stop()   // 정적 정지 프레임으로 복귀

   이미지 경로는 레이아웃에서 미리 주입:
     <script>window.OIIA_CAT_URL = '{{ "/assets/favicon/oiia-cat.png" | relative_url }}';</script>

   PNG 가 없거나 404 면 인라인 SVG 폴백 (간단한 주황 고양이) 으로 자동 전환.
*/
(function () {
  const SIZE = 64;            // 고해상도로 그리고 브라우저가 favicon 크기로 다운스케일
  const SPEED = 0.35;         // rad/frame — OIIA 처럼 빠르게 (60fps 기준 한바퀴 ~0.3s)
  const FRAME_RATE = 24;      // CPU 절약 위해 24fps 로 throttle

  const CAT_FALLBACK_SVG =
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">' +
      '<polygon points="20,35 28,12 38,32" fill="#e88a2e"/>' +
      '<polygon points="62,32 72,12 80,35" fill="#e88a2e"/>' +
      '<polygon points="24,32 30,18 36,30" fill="#ffd4a0"/>' +
      '<polygon points="64,30 70,18 76,32" fill="#ffd4a0"/>' +
      '<ellipse cx="50" cy="58" rx="36" ry="33" fill="#f29a3f"/>' +
      '<ellipse cx="50" cy="68" rx="22" ry="16" fill="#ffd4a0"/>' +
      '<ellipse cx="38" cy="54" rx="4.5" ry="5" fill="#1a1a1a"/>' +
      '<ellipse cx="62" cy="54" rx="4.5" ry="5" fill="#1a1a1a"/>' +
      '<circle cx="39" cy="53" r="1.3" fill="#fff"/>' +
      '<circle cx="63" cy="53" r="1.3" fill="#fff"/>' +
      '<path d="M50,67 L46,72 M50,67 L54,72" stroke="#1a1a1a" stroke-width="1.8" fill="none" stroke-linecap="round"/>' +
    '</svg>';

  function getOrCreateLink() {
    let link = document.querySelector("link[rel~='icon']");
    if (!link) {
      link = document.createElement('link');
      link.rel = 'icon';
      document.head.appendChild(link);
    }
    return link;
  }

  function loadImage() {
    return new Promise(function (resolve) {
      const img = new Image();
      img.onload = function () { resolve(img); };
      img.onerror = function () {
        // fallback: 인라인 SVG 데이터 URL — PNG 없을 때 폴백
        const svg = new Image();
        svg.onload = function () { resolve(svg); };
        svg.src = 'data:image/svg+xml;utf8,' + encodeURIComponent(CAT_FALLBACK_SVG);
      };
      // 레이아웃이 Jekyll relative_url 적용된 경로를 inline 으로 미리 주입한다
      img.src = window.OIIA_CAT_URL || '/assets/favicon/oiia-cat.png';
    });
  }

  const canvas = document.createElement('canvas');
  canvas.width = canvas.height = SIZE;
  const ctx = canvas.getContext('2d');
  const link = getOrCreateLink();

  let img = null;
  let angle = 0;
  let spinning = false;
  let lastFrame = 0;

  function drawAt(theta) {
    ctx.clearRect(0, 0, SIZE, SIZE);
    if (!img) return;
    ctx.save();
    ctx.translate(SIZE / 2, SIZE / 2);
    ctx.rotate(theta);
    ctx.drawImage(img, -SIZE / 2, -SIZE / 2, SIZE, SIZE);
    ctx.restore();
    link.href = canvas.toDataURL('image/png');
  }

  function tick(now) {
    if (!spinning) return;
    if (now - lastFrame >= 1000 / FRAME_RATE) {
      angle = (angle + SPEED) % (Math.PI * 2);
      drawAt(angle);
      lastFrame = now;
    }
    requestAnimationFrame(tick);
  }

  function start() {
    if (spinning) return;
    spinning = true;
    if (img) requestAnimationFrame(tick);
    else loadImage().then(function (i) { img = i; if (spinning) requestAnimationFrame(tick); });
  }
  function stop() {
    spinning = false;
    if (img) drawAt(0);  // 정적 frame (각도 0) 으로 리셋
  }

  window.faviconSpinner = { start: start, stop: stop };

  // 자동 동작: 페이지 로드되면 잠깐 회전 (UX 살리기) — window.load 까지 + 최소 800ms 보장
  const minSpin = 800;
  const startedAt = Date.now();
  start();
  function autoStop() {
    const elapsed = Date.now() - startedAt;
    setTimeout(stop, Math.max(0, minSpin - elapsed));
  }
  if (document.readyState === 'complete') autoStop();
  else window.addEventListener('load', autoStop);
})();
