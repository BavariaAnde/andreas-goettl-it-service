(() => {
  const header = document.querySelector('[data-header]');
  const menuToggle = document.querySelector('[data-menu-toggle]');
  const themeToggle = document.querySelector('[data-theme-toggle]');
  const nav = document.querySelector('.main-nav');
  const year = document.querySelector('[data-year]');
  const root = document.documentElement;
  const metaThemeColor = document.querySelector('meta[name="theme-color"]');

  const applyTheme = (theme) => {
    root.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);

    if (metaThemeColor) {
      metaThemeColor.setAttribute('content', theme === 'dark' ? '#0f3433' : '#f5f1e8');
    }

    if (themeToggle) {
      const icon = themeToggle.querySelector('.theme-toggle__icon');
      themeToggle.setAttribute('aria-label', theme === 'dark' ? 'Helles Design aktivieren' : 'Dunkles Design aktivieren');
      themeToggle.setAttribute('aria-pressed', String(theme === 'dark'));
      if (icon) {
        icon.textContent = theme === 'dark' ? '☀' : '☾';
      }
    }
  };

  const storedTheme = localStorage.getItem('theme');
  if (storedTheme === 'light' || storedTheme === 'dark') {
    applyTheme(storedTheme);
  } else {
    applyTheme('light');
  }

  const closeMenu = () => {
    header?.classList.remove('is-open');
    menuToggle?.setAttribute('aria-expanded', 'false');
    menuToggle?.setAttribute('aria-label', 'Navigation öffnen');
  };

  const openMenu = () => {
    header?.classList.add('is-open');
    menuToggle?.setAttribute('aria-expanded', 'true');
    menuToggle?.setAttribute('aria-label', 'Navigation schließen');
  };

  menuToggle?.addEventListener('click', () => {
    if (header?.classList.contains('is-open')) {
      closeMenu();
    } else {
      openMenu();
    }
  });

  themeToggle?.addEventListener('click', () => {
    const nextTheme = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    applyTheme(nextTheme);
  });

  nav?.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', closeMenu);
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
      closeMenu();
    }
  });

  window.addEventListener('resize', () => {
    if (window.innerWidth > 759) {
      closeMenu();
    }
  });

  if (year) {
    year.textContent = new Date().getFullYear();
  }

  // Sticky header shadow on scroll
  const updateHeaderShadow = () => {
    header?.classList.toggle('is-scrolled', window.scrollY > 8);
  };
  updateHeaderShadow();
  window.addEventListener('scroll', updateHeaderShadow, { passive: true });

  // Scroll-reveal for sections/cards
  const revealTargets = document.querySelectorAll('.reveal');
  if (revealTargets.length) {
    if ('IntersectionObserver' in window) {
      const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });

      revealTargets.forEach((target) => revealObserver.observe(target));
    } else {
      revealTargets.forEach((target) => target.classList.add('is-visible'));
    }
  }

  // Modal functionality
  const modalOpenButtons = document.querySelectorAll('[data-modal-open]');
  const modalCloseElements = document.querySelectorAll('[data-modal-close]');
  const modals = document.querySelectorAll('[data-modal]');

  const openModal = (modalId) => {
    const modal = document.getElementById(modalId);
    if (modal) {
      modal.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';

      // Focus first focusable element
      const firstFocusable = modal.querySelector('button, a');
      if (firstFocusable) {
        setTimeout(() => firstFocusable.focus(), 100);
      }
    }
  };

  const closeModal = (modal) => {
    if (modal) {
      modal.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    }
  };

  modalOpenButtons.forEach((button) => {
    button.addEventListener('click', () => {
      const modalId = button.getAttribute('data-modal-open');
      openModal(modalId);
    });
  });

  modalCloseElements.forEach((element) => {
    element.addEventListener('click', () => {
      const modal = element.closest('[data-modal]');
      closeModal(modal);
    });
  });

  // Close on Escape key
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
      modals.forEach((modal) => {
        if (modal.getAttribute('aria-hidden') === 'false') {
          closeModal(modal);
        }
      });
    }
  });
})();
