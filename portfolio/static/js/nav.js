const themeToggle = document.getElementById('theme-toggle');
const langToggle = document.getElementById('lang-toggle');

const currentTheme = localStorage.getItem('theme') || 'light';

if (currentTheme === 'dark') {
    document.body.classList.add('dark-mode');
    if (themeToggle) themeToggle.checked = false;
} else {
    document.body.classList.remove('dark-mode');
    if (themeToggle) themeToggle.checked = true;
}

themeToggle?.addEventListener('change', function() {
    if (this.checked) {
        document.body.classList.remove('dark-mode');
        localStorage.setItem('theme', 'light');
    } else {
        document.body.classList.add('dark-mode');
        localStorage.setItem('theme', 'dark');
    }
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