let currentIndex = 0;

function openLightbox(index) {
    currentIndex = index;
    document.getElementById('lightbox').classList.add('active');
    document.getElementById('lightbox-img').src = window.photos[currentIndex];
}

function closeLightbox() { document.getElementById('lightbox').classList.remove('active'); }

function changePhoto(dir) {
    currentIndex = (currentIndex + dir + window.photos.length) % window.photos.length;
    document.getElementById('lightbox-img').src = window.photos[currentIndex];
}

document.addEventListener('keydown', (e) => {
    if (!document.getElementById('lightbox').classList.contains('active')) return;
    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowLeft') changePhoto(-1);
    if (e.key === 'ArrowRight') changePhoto(1);
});

window.addEventListener('DOMContentLoaded', () => {
    const params = new URLSearchParams(window.location.search);
    if (params.has('lightbox')) openLightbox(parseInt(params.get('lightbox')));
});