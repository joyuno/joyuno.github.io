/* 클라이언트사이드 리스트 페이지네이션 — Jekyll plugin 안 쓰고 렌더된 카드만 보여줄 수 있어 GitHub Pages 호환.
   사용:
     <nav class="list-pagination" id="post-pagination" hidden>
       <button type="button" class="pg-btn" data-dir="prev">←</button>
       <span class="page-num"><span id="pg-cur">1</span> / <span id="pg-total">1</span></span>
       <button type="button" class="pg-btn" data-dir="next">→</button>
     </nav>
     <script>window.initListPagination({ itemSelector: '.post-card', pageSize: 30, navId: 'post-pagination' });</script>
*/
(function () {
  function initListPagination(opts) {
    const navId = opts.navId || 'post-pagination';
    const pageSize = opts.pageSize || 30;
    const items = Array.from(document.querySelectorAll(opts.itemSelector));
    const nav = document.getElementById(navId);
    if (!nav || items.length === 0) return;

    const total = Math.ceil(items.length / pageSize);
    if (total <= 1) return;

    let cur = 1;
    const elPrev = nav.querySelector('[data-dir="prev"]');
    const elNext = nav.querySelector('[data-dir="next"]');
    const elCur  = nav.querySelector('#pg-cur') || nav.querySelector('[data-pg="cur"]');
    const elTot  = nav.querySelector('#pg-total') || nav.querySelector('[data-pg="total"]');

    if (elTot) elTot.textContent = String(total);
    nav.hidden = false;

    function render(p) {
      cur = p;
      const start = (p - 1) * pageSize;
      const end = start + pageSize;
      items.forEach(function (el, i) {
        el.style.display = (i >= start && i < end) ? '' : 'none';
      });
      if (elCur) elCur.textContent = String(p);
      if (elPrev) elPrev.disabled = p === 1;
      if (elNext) elNext.disabled = p === total;
    }
    if (elPrev) elPrev.addEventListener('click', function () { if (cur > 1) { render(cur - 1); window.scrollTo({ top: 0, behavior: 'smooth' }); } });
    if (elNext) elNext.addEventListener('click', function () { if (cur < total) { render(cur + 1); window.scrollTo({ top: 0, behavior: 'smooth' }); } });
    render(1);
  }
  window.initListPagination = initListPagination;
})();
