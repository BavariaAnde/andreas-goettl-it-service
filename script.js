(() => {
  const root = document.documentElement;
  const header = document.querySelector('[data-header]');
  const themeToggle = document.querySelector('[data-theme-toggle]');
  const year = document.querySelector('[data-year]');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)');

  const storage = {
    get(key) {
      try {
        return localStorage.getItem(key);
      } catch (error) {
        return null;
      }
    },
    set(key, value) {
      try {
        localStorage.setItem(key, value);
      } catch (error) {}
    },
  };

  const systemTheme = () => (prefersDark.matches ? 'dark' : 'light');
  const currentTheme = () => root.dataset.theme || storage.get('theme') || systemTheme();

  const applyTheme = (theme, persist = false) => {
    root.dataset.theme = theme;
    root.style.colorScheme = theme;

    if (themeToggle) {
      const isDark = theme === 'dark';
      themeToggle.setAttribute('aria-pressed', String(isDark));
      themeToggle.setAttribute('aria-label', isDark ? 'Hellen Modus aktivieren' : 'Dunklen Modus aktivieren');
    }

    if (persist) {
      storage.set('theme', theme);
    }
  };

  applyTheme(currentTheme());

  themeToggle?.addEventListener('click', () => {
    applyTheme(currentTheme() === 'dark' ? 'light' : 'dark', true);
  });

  prefersDark.addEventListener?.('change', () => {
    if (!storage.get('theme')) {
      applyTheme(systemTheme());
    }
  });

  const updateHeader = () => {
    header?.classList.toggle('is-scrolled', window.scrollY > 8);
  };

  updateHeader();
  window.addEventListener('scroll', updateHeader, { passive: true });

  if (year) {
    year.textContent = new Date().getFullYear();
  }

  const revealItems = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, {
      rootMargin: '0px 0px -10% 0px',
      threshold: 0.12,
    });

    revealItems.forEach((item) => observer.observe(item));
  } else {
    revealItems.forEach((item) => item.classList.add('is-visible'));
  }
})();
