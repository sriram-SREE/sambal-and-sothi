// Sambal & Sothi - Native Book & Interactive Main JS
document.addEventListener('DOMContentLoaded', () => {
  initPreloader();
  initPageTransitions();
  initMobileNav();
  initNativeBookViewer();
  initReviewsSlider();
});

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

// 1. UNIFIED 4-PAGE SEAMLESS EMBLEM ZOOM & LOCK-IN PRELOADER ENGINE
function initPreloader() {
  const loader = document.getElementById('preloader');
  const chefContainer = document.querySelector('.preloader-chef-container');
  if (!loader || !chefContainer) return;

  const performLockIn = () => {
    chefContainer.classList.add('lock-to-header');
    setTimeout(() => {
      loader.classList.add('hidden');
      setTimeout(() => {
        if (loader.parentNode) loader.parentNode.removeChild(loader);
      }, 600);
    }, 380);
  };

  if (document.readyState === 'complete') {
    setTimeout(performLockIn, 550);
  } else {
    window.addEventListener('load', () => setTimeout(performLockIn, 550));
  }
  setTimeout(performLockIn, 1600);
}

// 2. UNIFIED SEAMLESS PAGE-TO-PAGE TRANSITION ENGINE
function initPageTransitions() {
  const iris = document.getElementById('iris-curtain');
  const ring = document.getElementById('ring-curtain');
  if (!iris || !ring) return;

  const isReduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  document.addEventListener('click', (e) => {
    const a = e.target.closest && e.target.closest('a[href]');
    if (!a) return;
    const href = a.getAttribute('href');
    if (!href || href.startsWith('#') || href.startsWith('tel:') || href.startsWith('mailto:') || a.target === '_blank' || /^https?:/i.test(href)) return;
    if (e.metaKey || e.ctrlKey || e.shiftKey) return;

    e.preventDefault();

    if (isReduced) {
      window.location.href = href;
      return;
    }

    const x = e.clientX || window.innerWidth / 2;
    const y = e.clientY || window.innerHeight / 2;
    const w = window.innerWidth;
    const h = window.innerHeight;
    const radius = Math.hypot(Math.max(x, w - x), Math.max(y, h - y)) * 1.08;

    iris.style.transition = 'none';
    iris.style.clipPath = `circle(0px at ${x}px ${y}px)`;
    iris.style.opacity = '1';

    ring.style.transition = 'none';
    ring.style.left = `${x}px`;
    ring.style.top = `${y}px`;
    ring.style.width = '0px';
    ring.style.height = '0px';
    ring.style.opacity = '0.95';

    requestAnimationFrame(() => {
      iris.style.transition = 'clip-path 520ms cubic-bezier(0.65, 0, 0.35, 1)';
      iris.style.clipPath = `circle(${radius}px at ${x}px ${y}px)`;

      ring.style.transition = 'width 520ms cubic-bezier(0.65, 0, 0.35, 1), height 520ms cubic-bezier(0.65, 0, 0.35, 1), opacity 520ms ease-out';
      ring.style.width = `${radius * 2.1}px`;
      ring.style.height = `${radius * 2.1}px`;
      ring.style.opacity = '0';
    });

    setTimeout(() => {
      window.location.href = href;
    }, 520);
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
      // Flipping forward: fromPage folds left (-180deg), revealing toPage underneath
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
      }, 650);

    } else if (currentPage < prevPageNum) {
      // Flipping backward: toPage turns in from left (-180deg) to 0deg
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
      }, 650);

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

  if (wrapper) {
    wrapper.addEventListener('click', (e) => {
      if (isFlipping) return;
      const rect = wrapper.getBoundingClientRect();
      const clickX = e.clientX - rect.left;
      if (clickX < rect.width / 2) {
        window.prevBookPage();
      } else {
        window.nextBookPage();
      }
    });

    // Touch swipe support for mobile
    let touchStartX = 0;
    wrapper.addEventListener('touchstart', (e) => {
      if (e.changedTouches && e.changedTouches[0]) {
        touchStartX = e.changedTouches[0].clientX;
      }
    }, { passive: true });

    wrapper.addEventListener('touchend', (e) => {
      if (isFlipping || !e.changedTouches || !e.changedTouches[0]) return;
      const touchEndX = e.changedTouches[0].clientX;
      const diffX = touchEndX - touchStartX;
      if (diffX < -40) {
        window.nextBookPage();
      } else if (diffX > 40) {
        window.prevBookPage();
      }
    }, { passive: true });
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
