// DOM XSS Sanitizer Helper
function escapeHtml(str) {
  if (str === null || str === undefined) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

document.addEventListener('DOMContentLoaded', () => {
  if (typeof window.SS_MENU === 'undefined' || !document.querySelector('.native-book-wrapper')) {
    return;
  }

  // Preserve authentic SVG menu pages or PHP rendered pages if already present
  if (document.querySelector('.native-book-wrapper .native-book-img') || document.querySelector('.native-book-wrapper .dynamic-cpt-page')) {
    return;
  }

  const wrapper = document.querySelector('.native-book-wrapper');
  const navContainer = document.getElementById('book-category-nav');
  const data = window.SS_MENU;
  const totalPages = data.totalPages || 13;
  const themeUrl = data.themeUrl || '';

  // 1. Group items by page
  const pageItems = {};
  const pageCategories = {};
  
  for (let i = 1; i <= totalPages; i++) {
    pageItems[i] = [];
    pageCategories[i] = [];
  }

  // Populate categories by page
  if (data.categoryPages) {
    for (const [cat, page] of Object.entries(data.categoryPages)) {
      if (!pageCategories[page]) {
         pageCategories[page] = [];
      }
      pageCategories[page].push(cat);
    }
  }

  // Populate items
  if (data.items && data.items.length) {
    data.items.forEach(item => {
      const page = data.categoryPages[item.category];
      if (page && pageItems[page]) {
        pageItems[page].push(item);
      }
    });
  }

  // 2. Build pages HTML
  let pagesHtml = '';
  
  for (let i = 1; i <= totalPages; i++) {
    let isActive = i === 1 ? ' active' : '';
    let pageClass = 'native-book-page';
    let content = '';

    if (i === 1) {
      pageClass += ' cover-page' + isActive;
      content = `<div class="book-cover-inner ornate-makkhan-cover">
  <div class="makkhan-border-frame">
    <div class="corner-flourish tl"></div>
    <div class="corner-flourish tr"></div>
    <div class="corner-flourish bl"></div>
    <div class="corner-flourish br"></div>
    
    <div class="cover-top-emblem">
      <img src="assets/img/brand-logo.png" alt="Sambal &amp; Sothi" class="book-cover-logo" style="width:75px;height:75px;object-fit:contain;margin-bottom:0.5rem;" />
    </div>
    
    <div class="cover-brand-header">
      <span class="cover-brand-sub">EST. LITTLE INDIA · 41 CHANDER ROAD</span>
      <h2 class="cover-brand-title">SAMBAL &amp; SOTHI</h2>
      <p class="cover-brand-desc">SINGAPORE STYLE INDIAN FOOD</p>
    </div>

    <div class="cover-title-divider">
      <span class="divider-line"></span>
      <span class="divider-symbol">❖</span>
      <span class="divider-line"></span>
    </div>

    <h1 class="cover-main-menu-text">M E N U</h1>

    <div class="cover-title-divider">
      <span class="divider-line"></span>
      <span class="divider-symbol">❖</span>
      <span class="divider-line"></span>
    </div>

    <div class="cover-footer-info">
      <p class="cover-address">41 Chander Road, Little India, Singapore 219543</p>
      <p class="cover-phone">Reservations: +65 8398 3865 / +65 8782 9193</p>
      <div class="cover-hours-badge">OPEN DAILY: 9:30 AM – 10:30 PM</div>
    </div>
  </div>
</div>`;
    } else if (i === totalPages) {
      pageClass += ' back-cover-page';
      content = `<div class="book-cover-inner ornate-makkhan-cover">
  <div class="makkhan-border-frame">
    <div class="corner-flourish tl"></div>
    <div class="corner-flourish tr"></div>
    <div class="corner-flourish bl"></div>
    <div class="corner-flourish br"></div>
    
    <div class="cover-top-emblem">
      <img src="assets/img/brand-logo.png" alt="Sambal &amp; Sothi" class="book-cover-logo" style="width:75px;height:75px;object-fit:contain;margin-bottom:0.5rem;" />
    </div>
    
    <div class="cover-brand-header">
      <span class="cover-brand-sub">EST. LITTLE INDIA · 41 CHANDER ROAD</span>
      <h2 class="cover-brand-title">SAMBAL &amp; SOTHI</h2>
      <p class="cover-brand-desc">SINGAPORE STYLE INDIAN FOOD</p>
    </div>

    <div class="cover-title-divider">
      <span class="divider-line"></span>
      <span class="divider-symbol">❖</span>
      <span class="divider-line"></span>
    </div>

    <h1 class="cover-main-menu-text">M E N U</h1>

    <div class="cover-title-divider">
      <span class="divider-line"></span>
      <span class="divider-symbol">❖</span>
      <span class="divider-line"></span>
    </div>

    <div class="cover-footer-info">
      <p class="cover-address">41 Chander Road, Little India, Singapore 219543</p>
      <p class="cover-phone">Reservations: +65 8398 3865 / +65 8782 9193</p>
      <div class="cover-hours-badge">OPEN DAILY: 9:30 AM – 10:30 PM</div>
    </div>
  </div>
</div>`;
    } else {
      
      const catIcons = {
        'Specials': '🌶️',
        'Sambal & Sothi Specials': '🌶️',
        'Indian Classic': '🥞',
        'Thosai': '🥞',
        'Fried Veg & Non-Veg': '🍤',
        'Prata': '🫓',
        'Kothu Prata & Egg Dishes': '🍳',
        'Gravy & Curry': '🍛',
        'Goreng': '🍜',
        'Briyani & Set Meals': '🍚',
        'Hot Drinks': '☕ 🫘',
        'Cold Drinks': '🍹 🧊'
      };
      let catNames = pageCategories[i] ? pageCategories[i].join(' &amp; ') : '';
      let catIcon = catIcons[catNames] || '❖';

      let itemsHtml = '';
      
      if (pageItems[i] && pageItems[i].length) {
        itemsHtml = pageItems[i].map(item => {
          let tagsHtml = '';
          if (item.tags && item.tags.length) {
            tagsHtml = '<div class="item-tags">' + item.tags.map(t => `<span class="item-tag">${escapeHtml(t)}</span>`).join('') + '</div>';
          }
          
          return `
            <div class="menu-page-item" data-tags="${(item.tags || []).join(',')}">
              <div class="menu-page-item-info">
                <span class="item-name">${escapeHtml(item.name)}</span>
                <span class="item-price">${escapeHtml(item.price)}</span>
              </div>
              <p class="item-desc">${escapeHtml(item.description)}</p>
              ${tagsHtml}
            </div>
          `;
        }).join('');
      }

      content = `
        <div class="page-header"><h2><span style='margin-right:8px;'>${catIcon}</span>${catNames}</h2></div>
        <div class="menu-page-items">${itemsHtml}</div>
      `;
    }

    pagesHtml += `<div class="${pageClass}" data-page="${i}">${content}</div>`;
  }

  // Inject pages
  wrapper.innerHTML = pagesHtml;

  // 3. Build Category Chips
  if (navContainer && data.categoryPages) {
    let chipsHtml = '';
    for (const [cat, page] of Object.entries(data.categoryPages)) {
        chipsHtml += `<button class="category-page-chip" data-page="${page}" onclick="if(typeof turnBookToPage === 'function') turnBookToPage(${page})">${cat}</button>`;
    }
    navContainer.innerHTML = chipsHtml;
  }

  // 4. Re-init book viewer
  // main.js may have already initialized the book on DOMContentLoaded with empty wrapper,
  // so we call it again now that the wrapper has content.
  if (typeof initNativeBookViewer === 'function') {
    initNativeBookViewer();
  }
});
