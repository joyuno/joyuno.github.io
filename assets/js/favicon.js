/* OIIA 고양이 파비콘 — sprite sheet 165 프레임 cycling 으로 진짜 OIIA 애니메이션 재현.
   Chrome/Safari 는 GIF/SVG 애니메이션 favicon 을 native 지원 안 함 → canvas 로 매 프레임 redraw.

   동작 정책:
   - idle 상태: 레이아웃 <link rel="icon" href=".../oiia-cat.png"> 로 박아둔 정지 프레임
   - 페이지 초기 로드 중: 프레임 cycling (window.load 이벤트까지, 최소 MIN_SPIN_MS)
   - 데이터 fetch 중: 명시적으로 start()/stop() 호출

   API:
     window.faviconSpinner.start()
     window.faviconSpinner.stop()

   레이아웃이 inline 으로 주입:
     <script>
       window.OIIA_CAT_URL    = '{{ "/assets/favicon/oiia-cat.png"    | relative_url }}';
       window.OIIA_SPRITE_URL = '{{ "/assets/favicon/oiia-sprite.png" | relative_url }}';
     </script>
*/
(function () {
  const FRAME_COUNT   = 165;
  const COLS          = 15;
  const FRAME_SIZE    = 64;
  const ANIMATION_FPS = 30;     // OIIA GIF 원본 ~30fps
  const MIN_SPIN_MS   = 1200;   // 빠른 로드에서도 회전 가시화 보장

  const STATIC_URL = window.OIIA_CAT_URL    || '/assets/favicon/oiia-cat.png';
  const SPRITE_URL = window.OIIA_SPRITE_URL || '/assets/favicon/oiia-sprite.png';

  function getOrCreateLink() {
    let link = document.querySelector("link[rel~='icon']");
    if (!link) {
      link = document.createElement('link');
      link.rel = 'icon';
      document.head.appendChild(link);
    }
    return link;
  }

  const link = getOrCreateLink();
  if (!link.href) link.href = STATIC_URL;

  const canvas = document.createElement('canvas');
  canvas.width = canvas.height = FRAME_SIZE;
  const ctx = canvas.getContext('2d');

  let sprite = null;
  let spinning = false;
  let spinStart = 0;
  let frameIdx = 0;
  let lastFrameTime = 0;
  let stopTimer = null;

  const spritePromise = new Promise(function (resolve) {
    const img = new Image();
    img.onload = function () { resolve(img); };
    img.onerror = function () { resolve(null); };
    img.src = SPRITE_URL;
  });
  spritePromise.then(function (s) { sprite = s; });

  function drawFrame(idx) {
    if (!sprite) return;
    const col = idx % COLS;
    const row = Math.floor(idx / COLS);
    ctx.clearRect(0, 0, FRAME_SIZE, FRAME_SIZE);
    ctx.drawImage(
      sprite,
      col * FRAME_SIZE, row * FRAME_SIZE, FRAME_SIZE, FRAME_SIZE,
      0, 0, FRAME_SIZE, FRAME_SIZE
    );
    link.href = canvas.toDataURL('image/png');
  }

  function tick(now) {
    if (!spinning) return;
    if (now - lastFrameTime >= 1000 / ANIMATION_FPS) {
      drawFrame(frameIdx);
      frameIdx = (frameIdx + 1) % FRAME_COUNT;
      lastFrameTime = now;
    }
    requestAnimationFrame(tick);
  }

  function start() {
    if (spinning) return;
    spinning = true;
    spinStart = Date.now();
    if (stopTimer) { clearTimeout(stopTimer); stopTimer = null; }
    if (sprite) requestAnimationFrame(tick);
    else spritePromise.then(function (s) {
      if (spinning && s) requestAnimationFrame(tick);
    });
  }

  function actuallyStop() {
    spinning = false;
    stopTimer = null;
    link.href = STATIC_URL;
  }

  function stop() {
    if (!spinning) { link.href = STATIC_URL; return; }
    const elapsed = Date.now() - spinStart;
    const delay = MIN_SPIN_MS - elapsed;
    if (delay > 0) {
      if (stopTimer) clearTimeout(stopTimer);
      stopTimer = setTimeout(actuallyStop, delay);
    } else {
      actuallyStop();
    }
  }

  window.faviconSpinner = { start: start, stop: stop };

  if (document.readyState !== 'complete') {
    start();
    window.addEventListener('load', stop, { once: true });
  }
})();
