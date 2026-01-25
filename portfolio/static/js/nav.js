const themeToggle = document.getElementById('theme-toggle');
const langToggle = document.getElementById('lang-toggle');

if (localStorage.getItem('theme') === 'light') {
    document.body.classList.add('light-mode');
    if (themeToggle) themeToggle.checked = true;
}

themeToggle?.addEventListener('change', function() {
    document.body.classList.toggle('light-mode', this.checked);
    localStorage.setItem('theme', this.checked ? 'light' : 'dark');
});

langToggle?.addEventListener('change', function() {
    const isLightboxActive = document.getElementById('lightbox')?.classList.contains('active');
    const scrollPosition = window.pageYOffset || document.documentElement.scrollTop;
    let p = window.location.pathname;
    let t = this.checked ? p.replace('/en/', '/') : p.replace('/galeria', '/en/gallery');
    if (!this.checked && t === '/') t = '/en/';
    setTimeout(() => {
        window.location.href = t + (isLightboxActive ? `?lightbox=${currentIndex}` : `?scroll=${scrollPosition}`);
    }, 450);
});