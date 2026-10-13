// Sambal & Sothi - Native Book & Interactive Main JS
document.addEventListener('DOMContentLoaded', () => {
  initPreloader();
  initPageTransitions();
  initMobileNav();
  initScrollHeader();
  initNativeBookViewer();
  initReviewsSlider();
  initCinemaScrollReveal();
  initDishLightbox();
  initLiveOpenStatus();
});

function initScrollHeader() {
  const header = document.querySelector('.site-header');
  if (!header) return;
  const onScroll = () => {
    if (window.scrollY > 24) {
      header.classList.add('is-scrolled');
    } else {
      header.classList.remove('is-scrolled');
    }
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}

// Category to Native Page Index Mapping (1-indexed)
const CATEGORY_PAGES = {
  'Specials': 2,
  'Indian Classic': 3,
  'Thosai': 4,
  'Fried Veg': 5,
  'Fried Non-Veg': 5,
  'Prata': 6,
  'Kothu Prata': 7,
  'Egg Dishes': 7,
  'Gravy & Curry': 8,
  'Goreng': 9,
  'Briyani': 10,
  'Set Meals': 10,
  'Hot Drinks': 11,
  'Cold Drinks': 12
};

let pageFlipAudioCtx = null;

// Synthetic Web Audio Paper Rustle (Zero-Latency Instant First Click Audio)
function playSyntheticFlipSound() {
  try {
    const AudioCtx = window.AudioContext || window.webkitAudioContext;
    if (!AudioCtx) return;
    if (!pageFlipAudioCtx) {
      pageFlipAudioCtx = new AudioCtx();
    }
    if (pageFlipAudioCtx.state === 'suspended') {
      pageFlipAudioCtx.resume();
    }

    const ctx = pageFlipAudioCtx;
    const now = ctx.currentTime;
    const duration = 0.26;

    const bufferSize = ctx.sampleRate * duration;
    const buffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
    const data = buffer.getChannelData(0);

    for (let i = 0; i < bufferSize; i++) {
      const t = i / bufferSize;
      const envelope = Math.sin(t * Math.PI) * Math.exp(-t * 3.0);
      data[i] = (Math.random() * 2 - 1) * envelope;
    }

    const noise = ctx.createBufferSource();
    noise.buffer = buffer;

    const filter = ctx.createBiquadFilter();
    filter.type = 'bandpass';
    filter.frequency.setValueAtTime(2000, now);
    filter.frequency.exponentialRampToValueAtTime(500, now + duration);
    filter.Q.value = 1.8;

    const gain = ctx.createGain();
    gain.gain.setValueAtTime(0.01, now);
    gain.gain.linearRampToValueAtTime(1.0, now + 0.02);
    gain.gain.exponentialRampToValueAtTime(0.01, now + duration);

    noise.connect(filter);
    filter.connect(gain);
    gain.connect(ctx.destination);

    noise.start(now);
    noise.stop(now + duration);
  } catch (e) {}
}

// Master Page Flip Sound Trigger (Fires on Very First Click)
function playPaperFlipSound() {
  // 1. Instant Web Audio synth sound (Guaranteed on 1st click)
  playSyntheticFlipSound();

  // 2. HTML5 MP3 / WAV audio file trigger
  try {
    const base = window.SS_THEME_URI || '';
    const mp3 = base ? base + '/assets/audio/page-flip.mp3' : 'assets/audio/page-flip.mp3';
    const wav = base ? base + '/assets/audio/page-flip.wav' : 'assets/audio/page-flip.wav';
    const a = new Audio(mp3);
    a.volume = 0.9;
    const p = a.play();
    if (p && p.catch) {
      p.catch(() => {
        const w = new Audio(wav);
        w.volume = 0.9;
        w.play().catch(() => {});
      });
    }
  } catch (err) {}
}

// Pre-unlock Web Audio API context on any initial user pointer gesture
document.addEventListener('pointerdown', () => {
  try {
    const AudioCtx = window.AudioContext || window.webkitAudioContext;
    if (AudioCtx) {
      if (!pageFlipAudioCtx) pageFlipAudioCtx = new AudioCtx();
      if (pageFlipAudioCtx.state === 'suspended') pageFlipAudioCtx.resume();
    }
  } catch(e) {}
}, { once: true });

// 1. ROYAL BANANA LEAF PRELOADER & GOLD IRIS APERTURE ENGINE
function initPreloader() {
  const pl = document.getElementById('ss-preloader');
  if (!pl) return;

  const root = document.documentElement;
  const edge = pl.querySelector('.ss-edge');
  const reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Split the wordmark into masked letters with staggered reveal
  let idx = 0;
  pl.querySelectorAll('.ss-word .w, .ss-word .amp').forEach((el) => {
    const t = el.textContent;
    el.textContent = '';
    for (let k = 0; k < t.length; k++) {
      const m = document.createElement('span');
      m.className = 'ss-ch';
      const c = document.createElement('i');
      c.textContent = t[k];
      c.style.setProperty('--i', idx++);
      m.appendChild(c);
      el.appendChild(m);
    }
  });

  let first = true;
  try {
    first = sessionStorage.getItem('ss-visited') !== '1';
    sessionStorage.setItem('ss-visited', '1');
  } catch (e) {}

  if (!first) pl.classList.add('is-quick');
  const S = first ? 1 : 0.5;
  const MIN = parseInt(pl.getAttribute('data-min') || (first ? '2100' : '900'), 10);
  const MAX = 4500;
  root.classList.add('ss-loading');
  const start = (typeof performance !== 'undefined' && performance.now) ? performance.now() : Date.now();
  let leaving = false;

  function easeQ(k) { return k < 0.5 ? 8 * k * k * k * k : 1 - Math.pow(-2 * k + 2, 4) / 2; }

  function tween(dur, delay, step, done) {
    setTimeout(() => {
      const t0 = (typeof performance !== 'undefined' && performance.now) ? performance.now() : Date.now();
      function f(now) {
        const k = Math.min(1, (now - t0) / dur);
        step(k);
        if (k < 1) requestAnimationFrame(f);
        else if (done) done();
      }
      requestAnimationFrame(f);
    }, delay || 0);
  }

  function farthest(cx, cy) {
    return Math.hypot(Math.max(cx, window.innerWidth - cx), Math.max(cy, window.innerHeight - cy)) + 36;
  }

  function iris(cx, cy, a, b, dur, done) {
    pl.style.setProperty('--cx', cx + 'px');
    pl.style.setProperty('--cy', cy + 'px');
    tween(dur, 0, (k) => {
      const r = a + (b - a) * easeQ(k);
      const er = r + 3;
      pl.style.setProperty('--r', r + 'px');
      if (edge) {
        edge.style.width = edge.style.height = (er * 2) + 'px';
        edge.style.transform = 'translate(' + (cx - er) + 'px,' + (cy - er) + 'px)';
        edge.style.opacity = a < b ? String(1 - Math.pow(k, 3)) : String(Math.min(1, (1 - k) * 4 + 0.2));
      }
    }, done);
  }

  function leave() {
    if (leaving) return;
    leaving = true;
    const nowTime = (typeof performance !== 'undefined' && performance.now) ? performance.now() : Date.now();
    const wait = Math.max(0, MIN - (nowTime - start));

    setTimeout(() => {
      pl.classList.add('is-out');
      if (reduce) {
        pl.style.transition = 'opacity 0.4s ease';
        pl.style.opacity = '0';
        root.classList.remove('ss-loading');
        setTimeout(() => {
          pl.classList.add('is-done');
          pl.style.display = 'none';
        }, 420);
        return;
      }

      const hold = 420;
      setTimeout(() => {
        const seal = pl.querySelector('.ss-seal') || pl.querySelector('.ss-c');
        const rc = seal ? seal.getBoundingClientRect() : { left: window.innerWidth / 2 - 30, top: window.innerHeight / 2 - 30, width: 60, height: 60 };
        const cx = rc.left + rc.width / 2;
        const cy = rc.top + rc.height / 2;
        pl.style.setProperty('--r', '0px');
        pl.classList.add('is-iris');
        root.classList.remove('ss-loading');

        iris(cx, cy, 0, farthest(cx, cy), 950, () => {
          pl.classList.add('is-done');
          pl.classList.remove('is-iris');
          pl.style.display = 'none';
        });
      }, hold);
    }, wait);
  }

  if (document.readyState === 'complete') {
    leave();
  } else {
    window.addEventListener('load', leave);
  }
  setTimeout(leave, MAX);

  window.addEventListener('pageshow', (e) => {
    if (e.persisted) {
      pl.className = 'is-out is-done';
      pl.style.display = 'none';
      root.classList.remove('ss-loading');
    }
  });
}

// 2. SILKY EDITORIAL PAGE-TO-PAGE NAVIGATION ENGINE (Zero Door Slamming, Instant & Regal)
function initPageTransitions() {
  document.body.classList.remove('ss-page-exiting');

  window.addEventListener('pageshow', () => {
    document.body.classList.remove('ss-page-exiting');
  });

  const isReduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  document.addEventListener('click', (e) => {
    const a = e.target.closest && e.target.closest('a[href]');
    if (!a) return;
    const href = a.getAttribute('href');
    if (!href || href.startsWith('#') || href.startsWith('tel:') || href.startsWith('mailto:') || a.target === '_blank' || /^https?:/i.test(href)) return;
    if (e.metaKey || e.ctrlKey || e.shiftKey) return;

    // Same-page click: do nothing
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    const targetPath = href.split('?')[0].split('#')[0].split('/').pop() || 'index.html';
    if (currentPath === targetPath) return;

    e.preventDefault();

    if (isReduced) {
      window.location.href = href;
      return;
    }

    document.body.classList.add('ss-page-exiting');
    setTimeout(() => {
      window.location.href = href;
    }, 180);
  });
}

// 3. Mobile Navigation Drawer Toggle
function initMobileNav() {
  const burger = document.getElementById('burger-btn');
  const drawer = document.getElementById('mobile-nav');
  const closeBtn = document.getElementById('mobile-nav-close');

  if (burger && drawer) {
    burger.addEventListener('click', () => drawer.classList.add('active'));
  }
  if (closeBtn && drawer) {
    closeBtn.addEventListener('click', () => drawer.classList.remove('active'));
  }
  if (drawer) {
    drawer.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => drawer.classList.remove('active'));
    });
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && drawer.classList.contains('active')) {
        drawer.classList.remove('active');
      }
    });
  }
}

// 4. Native Pure 3D PageFlip Book Viewer with Instant First-Click Audio
function initNativeBookViewer() {
  const pages = document.querySelectorAll('.native-book-page');
  const countSpan = document.getElementById('book-page-indicator');
  const wrapper = document.getElementById('native-book-wrapper') || document.querySelector('.native-book-wrapper');
  if (!pages.length) return;

  let currentPage = 1;
  const totalPages = pages.length;
  let isFlipping = false;

  function updatePageDisplay(targetPage, playAudio = true) {
    if (isFlipping) return;
    targetPage = Math.max(1, Math.min(totalPages, targetPage));
    if (targetPage === currentPage && targetPage !== 1) return;

    if (playAudio) {
      playPaperFlipSound();
    }

    const prevPageNum = currentPage;
    currentPage = targetPage;

    const fromPage = pages[prevPageNum - 1];
    const toPage = pages[currentPage - 1];

    if (currentPage > prevPageNum) {
      // Flipping forward: fromPage folds left (-95deg + smooth fade), revealing toPage underneath
      isFlipping = true;

      toPage.classList.remove('flipped', 'flipping-forward', 'flipping-backward', 'flip-in');
      toPage.classList.add('underneath');

      for (let i = 0; i < currentPage - 1; i++) {
        if (i !== prevPageNum - 1) {
          pages[i].classList.remove('active', 'underneath');
          pages[i].classList.add('flipped');
        }
      }

      fromPage.classList.remove('active');
      fromPage.classList.add('flipping-forward');

      setTimeout(() => {
        fromPage.classList.remove('flipping-forward');
        fromPage.classList.add('flipped');
        toPage.classList.remove('underneath');
        toPage.classList.add('active');
        isFlipping = false;
        refreshUI();
      }, 500);

    } else if (currentPage < prevPageNum) {
      // Flipping backward: toPage turns in from left (-95deg) to 0deg
      isFlipping = true;

      for (let i = currentPage; i < totalPages; i++) {
        if (i !== prevPageNum - 1) {
          pages[i].classList.remove('active', 'flipped', 'underneath');
        }
      }

      toPage.classList.remove('flipped', 'active', 'underneath');
      toPage.classList.add('flipping-backward');

      void toPage.offsetWidth; // Force reflow

      toPage.classList.add('flip-in');

      setTimeout(() => {
        toPage.classList.remove('flipping-backward', 'flip-in');
        toPage.classList.add('active');
        fromPage.classList.remove('active');
        isFlipping = false;
        refreshUI();
      }, 500);

    } else {
      // Initial state
      pages.forEach((p, idx) => {
        p.classList.remove('active', 'flipped', 'underneath', 'flipping-forward', 'flipping-backward', 'flip-in');
        if (idx === 0) {
          p.classList.add('active');
        }
      });
      refreshUI();
    }
  }

  function refreshUI() {
    if (countSpan) {
      countSpan.textContent = `Page ${currentPage} of ${totalPages}`;
    }

    const prevBtn = document.getElementById('btn-prev-page');
    const nextBtn = document.getElementById('btn-next-page');
    if (prevBtn) prevBtn.style.opacity = currentPage === 1 ? '0.5' : '1';
    if (nextBtn) nextBtn.style.opacity = currentPage === totalPages ? '0.5' : '1';

    document.querySelectorAll('.category-page-chip').forEach(chip => {
      const p = parseInt(chip.dataset.page || '0', 10);
      chip.classList.toggle('active', p === currentPage);
    });
  }

  window.turnBookToPage = (page) => {
    updatePageDisplay(page, true);
  };

  window.nextBookPage = () => {
    if (currentPage < totalPages && !isFlipping) {
      updatePageDisplay(currentPage + 1, true);
    }
  };

  window.prevBookPage = () => {
    if (currentPage > 1 && !isFlipping) {
      updatePageDisplay(currentPage - 1, true);
    }
  };

  // Smart Left/Right Empty-Area Tap Turn (Blocks accidental turns while scrolling or touching dishes/buttons)
  if (wrapper && !window.__ssSmartBookTapBound) {
    window.__ssSmartBookTapBound = true;
    let pDownX = 0;
    let pDownY = 0;
    let pDownTime = 0;
    let pDownScrollY = 0;
    let pMoved = false;
    let lastScrollTs = 0;

    const recordScroll = () => { lastScrollTs = Date.now(); pMoved = true; };
    window.addEventListener('scroll', recordScroll, { passive: true });
    wrapper.addEventListener('scroll', recordScroll, { capture: true, passive: true });

    wrapper.addEventListener('pointerdown', (e) => {
      if (e.isPrimary === false) { pMoved = true; return; }
      pDownX = e.clientX;
      pDownY = e.clientY;
      pDownTime = Date.now();
      pDownScrollY = window.scrollY;
      pMoved = false;
    }, { passive: true });

    wrapper.addEventListener('pointermove', (e) => {
      if (Math.abs(e.clientX - pDownX) > 7 || Math.abs(e.clientY - pDownY) > 7) {
        pMoved = true;
      }
    }, { passive: true });

    wrapper.addEventListener('pointerup', (e) => {
      if (pMoved || isFlipping) return;
      const now = Date.now();
      const duration = now - pDownTime;
      const dx = Math.abs(e.clientX - pDownX);
      const dy = Math.abs(e.clientY - pDownY);
      const scrollDiff = Math.abs(window.scrollY - pDownScrollY);

      // 1. Block if scrolling occurred, finger moved > 7px, or hold lasted > 300ms
      if (dx > 7 || dy > 7 || scrollDiff > 2 || duration > 300 || (now - lastScrollTs) < 400) {
        return;
      }

      // 2. Block if user touched dish text, price, description, tag, header, or interactive element
      if (e.target && e.target.closest && e.target.closest('a, button, input, select, textarea, .item-name, .item-price, .item-desc, .item-tag, .page-header h2')) {
        return;
      }

      // 3. Only turn page when tapping empty area on the Left (< 30%) or Right (> 70%) side
      const rect = wrapper.getBoundingClientRect();
      if (!rect.width) return;
      const relX = (e.clientX - rect.left) / rect.width;

      if (relX > 0.70) {
        window.nextBookPage();
      } else if (relX < 0.30) {
        window.prevBookPage();
      }
    });
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight') window.nextBookPage();
    if (e.key === 'ArrowLeft') window.prevBookPage();
  });

  updatePageDisplay(1, false);
}



// 5. Customer Reviews Swipeable Carousel Engine
function initReviewsSlider() {
  const slider = document.getElementById('reviews-slider');
  const track = document.getElementById('reviews-track');
  const prevBtn = document.getElementById('review-prev-btn');
  const nextBtn = document.getElementById('review-next-btn');
  const dotsContainer = document.getElementById('reviews-dots');
  if (!slider || !track) return;

  const cards = track.querySelectorAll('.review-card');
  if (!cards.length) return;

  // Build pagination dots
  if (dotsContainer) {
    dotsContainer.innerHTML = '';
    cards.forEach((card, idx) => {
      const dot = document.createElement('button');
      dot.type = 'button';
      dot.className = 'review-dot' + (idx === 0 ? ' active' : '');
      dot.setAttribute('aria-label', 'Go to review ' + (idx + 1));
      dot.addEventListener('click', () => {
        scrollToIndex(idx);
      });
      dotsContainer.appendChild(dot);
    });
  }

  const dots = dotsContainer ? dotsContainer.querySelectorAll('.review-dot') : [];

  function getStep() {
    if (cards.length > 0) {
      const gap = parseInt(window.getComputedStyle(track).gap || '28', 10);
      return cards[0].offsetWidth + gap;
    }
    return 340;
  }

  function updateUI() {
    const scrollLeft = slider.scrollLeft;
    const maxScroll = slider.scrollWidth - slider.clientWidth;

    let activeIdx = 0;
    let minDiff = Infinity;
    cards.forEach((card, idx) => {
      const diff = Math.abs(card.offsetLeft - track.offsetLeft - scrollLeft);
      if (diff < minDiff) {
        minDiff = diff;
        activeIdx = idx;
      }
    });

    dots.forEach((dot, idx) => {
      dot.classList.toggle('active', idx === activeIdx);
    });

    if (prevBtn) prevBtn.disabled = scrollLeft <= 10;
    if (nextBtn) nextBtn.disabled = scrollLeft >= maxScroll - 10;
  }

  function scrollToIndex(idx) {
    if (idx >= 0 && idx < cards.length) {
      const targetLeft = cards[idx].offsetLeft - track.offsetLeft;
      slider.scrollTo({
        left: targetLeft,
        behavior: 'smooth'
      });
    }
  }

  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      slider.scrollBy({ left: -getStep(), behavior: 'smooth' });
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      slider.scrollBy({ left: getStep(), behavior: 'smooth' });
    });
  }

  // Pointer / Mouse Drag Support (Desktop & Touch)
  let isDown = false;
  let startX = 0;
  let scrollStart = 0;

  slider.addEventListener('pointerdown', (e) => {
    isDown = true;
    startX = e.pageX;
    scrollStart = slider.scrollLeft;
    slider.style.scrollBehavior = 'auto';
  });

  window.addEventListener('pointermove', (e) => {
    if (!isDown) return;
    const dist = e.pageX - startX;
    slider.scrollLeft = scrollStart - dist;
  });

  window.addEventListener('pointerup', () => {
    if (isDown) {
      isDown = false;
      slider.style.scrollBehavior = 'smooth';
      setTimeout(updateUI, 120);
    }
  });

  slider.addEventListener('pointercancel', () => {
    if (isDown) {
      isDown = false;
      slider.style.scrollBehavior = 'smooth';
      setTimeout(updateUI, 120);
    }
  });

  // Keyboard navigation
  slider.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight') {
      e.preventDefault();
      slider.scrollBy({ left: getStep(), behavior: 'smooth' });
    } else if (e.key === 'ArrowLeft') {
      e.preventDefault();
      slider.scrollBy({ left: -getStep(), behavior: 'smooth' });
    }
  });

  let scrollTimeout = null;
  slider.addEventListener('scroll', () => {
    if (scrollTimeout) cancelAnimationFrame(scrollTimeout);
    scrollTimeout = requestAnimationFrame(updateUI);
  }, { passive: true });

  updateUI();
  window.addEventListener('resize', updateUI);
}

// 6. Unified Silk Editorial Scroll Glide (Zero Mobile Blank Gap & Zero Layer-Drop Flicker)
function initCinemaScrollReveal() {
  const isReduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (isReduced || !('IntersectionObserver' in window)) return;

  const revealTargets = [];

  document.querySelectorAll(
    '.artisanal-header, .artisanal-row, .social-band-header, .social-card, .reviews-header, .review-card, .about-story-grid, .dishes-section .section-header-flex, .dish-card, .contact-card-box, .contact-map-box, .footer-grid'
  ).forEach((el) => {
    const rect = el.getBoundingClientRect();
    // Only add .ss-reveal to elements below the initial viewport so above-the-fold never flashes
    if (rect.top >= window.innerHeight * 0.92) {
      el.classList.add('ss-reveal');
      revealTargets.push(el);
    }
  });

  if (!revealTargets.length) return;

  const observer = new IntersectionObserver(
    (entries, obs) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          obs.unobserve(entry.target);
          entry.target.classList.add('is-visible');
        }
      });
    },
    {
      threshold: 0.02,
      rootMargin: '0px 0px -15px 0px'
    }
  );

  revealTargets.forEach((el) => observer.observe(el));
}

// 7. Interactive HD Dish Lightbox Modal on Featured Dish Cards
function initDishLightbox() {
  const dishCards = document.querySelectorAll('.dish-card.has-dish-image');
  if (!dishCards.length) return;

  let lightbox = document.getElementById('ss-dish-lightbox');
  if (!lightbox) {
    lightbox = document.createElement('div');
    lightbox.id = 'ss-dish-lightbox';
    lightbox.className = 'ss-lightbox-overlay ss-dish-lightbox';
    lightbox.setAttribute('role', 'dialog');
    lightbox.setAttribute('aria-modal', 'true');
    lightbox.setAttribute('aria-label', 'Signature Dish Preview');

    lightbox.innerHTML = `
      <div class="ss-lightbox-modal">
        <span class="corner-flourish tl" aria-hidden="true"></span>
        <span class="corner-flourish tr" aria-hidden="true"></span>
        <span class="corner-flourish bl" aria-hidden="true"></span>
        <span class="corner-flourish br" aria-hidden="true"></span>
        <button type="button" class="ss-lightbox-close" aria-label="Close dish preview">&times;</button>
        <div class="ss-lightbox-img-wrap">
          <img src="" alt="" class="ss-lightbox-img" id="ss-lightbox-img">
        </div>
        <div class="ss-lightbox-header">
          <div>
            <span class="ss-lightbox-cat" id="ss-lightbox-tag">CHEF'S SIGNATURE SELECTION</span>
            <h3 class="ss-lightbox-title" id="ss-lightbox-title"></h3>
          </div>
          <div class="dish-price-tag" id="ss-lightbox-price"></div>
        </div>
        <div class="ss-lightbox-tags" id="ss-lightbox-badges"></div>
        <div class="ss-lightbox-actions">
          <a href="tel:+6583983865" class="btn-primary" style="padding: 0.75rem 1.5rem; font-size: 0.8rem;">&#9990; Call to Order / Reserve</a>
          <button type="button" class="btn-secondary ss-lightbox-dismiss" style="padding: 0.75rem 1.5rem; font-size: 0.8rem; cursor: pointer;">Close Preview</button>
        </div>
      </div>
    `;
    document.body.appendChild(lightbox);
  }

  const imgEl = document.getElementById('ss-lightbox-img');
  const tagEl = document.getElementById('ss-lightbox-tag');
  const titleEl = document.getElementById('ss-lightbox-title');
  const priceEl = document.getElementById('ss-lightbox-price');
  const badgesEl = document.getElementById('ss-lightbox-badges');
  const closeBtn = lightbox.querySelector('.ss-lightbox-close');
  const dismissBtn = lightbox.querySelector('.ss-lightbox-dismiss');

  const closeLightbox = () => {
    lightbox.classList.remove('active');
    document.body.style.overflow = '';
  };

  const openLightbox = (card) => {
    const cardImg = card.querySelector('img.dish-card-img, .dish-card-img-box img, .dish-card-img img');
    const cardCat = card.querySelector('.dish-category');
    const cardTitle = card.querySelector('.dish-title, .dish-name');
    const cardPrice = card.querySelector('.dish-price-tag, .dish-price');
    const cardBadges = card.querySelector('.dish-tags-list');

    if (cardImg && imgEl) {
      imgEl.src = cardImg.getAttribute('src') || '';
      imgEl.alt = cardImg.getAttribute('alt') || (cardTitle ? cardTitle.textContent.trim() : 'Signature Dish');
    }
    if (tagEl) {
      tagEl.textContent = cardCat ? cardCat.textContent.trim().toUpperCase() : "CHEF'S SIGNATURE SELECTION";
    }
    if (titleEl && cardTitle) titleEl.textContent = cardTitle.textContent.trim();
    if (priceEl && cardPrice) priceEl.textContent = cardPrice.textContent.trim();
    if (badgesEl) {
      badgesEl.innerHTML = cardBadges ? cardBadges.innerHTML : '';
    }

    lightbox.classList.add('active');
    document.body.style.overflow = 'hidden';
  };

  dishCards.forEach((card) => {
    card.setAttribute('tabindex', '0');
    card.setAttribute('role', 'button');
    const dishTitle = card.querySelector('.dish-title, .dish-name');
    if (dishTitle) {
      card.setAttribute('aria-label', `Inspect ${dishTitle.textContent.trim()} in high definition`);
    }
    card.addEventListener('click', (e) => {
      if (e.target && e.target.closest('a, button')) return;
      openLightbox(card);
    });
    card.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        openLightbox(card);
      }
    });
  });

  if (closeBtn) closeBtn.addEventListener('click', closeLightbox);
  if (dismissBtn) dismissBtn.addEventListener('click', closeLightbox);

  lightbox.addEventListener('click', (e) => {
    if (e.target === lightbox) closeLightbox();
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && lightbox.classList.contains('active')) {
      closeLightbox();
    }
  });
}

// 8. Live Singapore Time (SGT / UTC+8) "OPEN NOW" Status Indicator
function initLiveOpenStatus() {
  try {
    const now = new Date();
    let sgtHours = 12;
    let sgtMinutes = 0;

    try {
      const parts = new Intl.DateTimeFormat('en-US', {
        timeZone: 'Asia/Singapore',
        hour: 'numeric',
        minute: 'numeric',
        hour12: false
      }).formatToParts(now);

      parts.forEach((p) => {
        if (p.type === 'hour') sgtHours = parseInt(p.value, 10) % 24;
        if (p.type === 'minute') sgtMinutes = parseInt(p.value, 10);
      });
    } catch (err) {
      const utcMs = now.getTime() + now.getTimezoneOffset() * 60000;
      const sgtDate = new Date(utcMs + 8 * 3600000);
      sgtHours = sgtDate.getHours();
      sgtMinutes = sgtDate.getMinutes();
    }

    const totalMinutes = sgtHours * 60 + sgtMinutes;
    // Daily operating hours: 9:00 AM (540m) to 10:30 PM (1350m) SGT
    const isOpen = totalMinutes >= 540 && totalMinutes < 1350;

    const createBadge = () => {
      const badge = document.createElement('span');
      badge.className = `ss-live-status-badge ${isOpen ? 'is-open' : 'is-closed'}`;
      badge.innerHTML = `<span class="ss-status-dot" aria-hidden="true"></span><span>${
        isOpen ? 'OPEN NOW · SGT' : 'CLOSED · OPENS 9:00 AM SGT'
      }</span>`;
      return badge;
    };

    // 1. Inject into Contact Page "TIMINGS & OPENING HOURS" item
    document.querySelectorAll('.contact-info-item').forEach((item) => {
      const label = item.querySelector('.contact-info-label');
      if (label && /opening hours|timings/i.test(label.textContent) && !item.querySelector('.ss-live-status-badge')) {
        const wrap = document.createElement('div');
        wrap.style.marginTop = '10px';
        wrap.appendChild(createBadge());
        item.appendChild(wrap);
      }
    });

    // 2. Inject into Footer column with "Open Daily:"
    document.querySelectorAll('.footer-grid > div, .footer-col').forEach((col) => {
      if (/open daily|operating hours/i.test(col.textContent) && !col.querySelector('.ss-live-status-badge')) {
        const wrap = document.createElement('div');
        wrap.style.marginTop = '10px';
        wrap.appendChild(createBadge());
        col.appendChild(wrap);
      }
    });

    // 3. Inject into Concierge Mobile Drawer footer
    const mobFooter = document.querySelector('.mobile-nav-footer');
    if (mobFooter && !mobFooter.querySelector('.ss-live-status-badge')) {
      const wrap = document.createElement('div');
      wrap.style.marginTop = '6px';
      wrap.style.display = 'flex';
      wrap.style.justifyContent = 'center';
      wrap.appendChild(createBadge());
      mobFooter.appendChild(wrap);
    }
  } catch (e) {}
}

