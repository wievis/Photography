let currentIndex = 0;

function openLightbox(index) {
    currentIndex = index;
    updateLightboxContent();
    document.getElementById('lightbox').classList.add('active');
}

function closeLightbox() { document.getElementById('lightbox').classList.remove('active'); }

function changePhoto(dir) {
    currentIndex = (currentIndex + dir + window.photos.length) % window.photos.length;
    updateLightboxContent();
}

function updateLightboxContent() {
    const photo = window.photos[currentIndex];
    document.getElementById('lightbox-img').src = photo.thumb;
    
    const downloadBtn = document.getElementById('download-btn');
    downloadBtn.onclick = (e) => {
        e.preventDefault();
        downloadImage(photo.full);
    };
}

async function downloadImage(url) {
    try {
        const response = await fetch(url);
        const blob = await response.blob();
        const blobUrl = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = blobUrl;
        a.download = url.split('/').pop(); // Nazwa pliku z adresu URL
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        window.URL.revokeObjectURL(blobUrl);
    } catch (error) {
        window.open(url, '_blank'); // Backup: otwarcie w nowej karcie jeśli fetch zawiedzie
    }
}

document.addEventListener('keydown', (e) => {
    if (!document.getElementById('lightbox').classList.contains('active')) return;
    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowLeft') changePhoto(-1);
    if (e.key === 'ArrowRight') changePhoto(1);
});