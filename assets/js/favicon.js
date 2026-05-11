/* 회전하는 OIIA 고양이 파비콘 — canvas 로 매 프레임 favicon URL 갱신.
   Chrome/Safari 는 GIF/SVG 애니메이션 favicon 을 native 지원 안 함 → JS swap 이 유일.

   동작 정책:
   - idle 상태(평소): 레이아웃이 <link rel="icon" href=".../oiia-cat.gif"> 로 박아둔 정적 파비콘.
     Chrome/Safari 에서는 GIF 첫 프레임이 멈춰 보이고, Firefox 에서는 자연스럽게 애니메이션 됨.
   - 페이지 초기 로드(HTML/asset 다운로드 중): 회전 (window.load 이벤트까지).
   - 데이터 fetch 중: 명시적으로 start()/stop() 호출.

   API:
     window.faviconSpinner.start()
     window.faviconSpinner.stop()   // 정적 GIF URL 로 복귀

   이미지 경로는 레이아웃이 inline 으로 주입:
     <script>window.OIIA_CAT_URL = '{{ "/assets/favicon/oiia-cat.gif" | relative_url }}';</script>
*/
(function () {
  const SIZE = 64;
  const SPEED = 0.35;
  const FRAME_RATE = 24;

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

  const STATIC_URL = window.OIIA_CAT_URL || '/assets/favicon/oiia-cat.gif';

  function loadImage() {
    return new Promise(function (resolve) {
      const img = new Image();
      img.onload = function () { resolve(img); };
      img.onerror = function () {
        const svg = new Image();
        svg.onload = function () { resolve(svg); };
        svg.src = 'data:image/svg+xml;utf8,' + encodeURIComponent(CAT_FALLBACK_SVG);
      };
      img.src = STATIC_URL;
    });
  }

  const canvas = document.createElement('canvas');
  canvas.width = canvas.height = SIZE;
  const ctx = canvas.getContext('2d');
  const link = getOrCreateLink();
  if (!link.href) link.href = STATIC_URL;

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
    link.href = STATIC_URL;
  }

  window.faviconSpinner = { start: start, stop: stop };

  if (document.readyState !== 'complete') {
    start();
    window.addEventListener('load', stop, { once: true });
  }
})();
