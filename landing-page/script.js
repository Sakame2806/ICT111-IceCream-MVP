async function loadLatestArtwork() {
  try {
    const response = await fetch('/api/homepage', { cache: 'no-store' });
    const data = await response.json();
    if (!response.ok || !data.newest?.length) return;
    const artwork = data.newest[0];
    document.getElementById('hero-art-image').style.backgroundImage =
      `linear-gradient(rgba(12,30,46,.05), rgba(12,30,46,.12)), url("${artwork.image_url}")`;
    document.querySelector('.image-fallback').hidden = true;
    document.getElementById('hero-art-title').textContent = artwork.title;
    document.getElementById('hero-like-count').textContent = `♡ ${artwork.like_count}`;
    document.querySelector('.main-preview').addEventListener('click', () => {
      window.location.href = `/Artwork.html?art_id=${encodeURIComponent(artwork.art_id)}`;
    });
    document.querySelector('.main-preview').style.cursor = 'pointer';
  } catch {
    // The branded fallback remains visible when the local API is unavailable.
  }
}

loadLatestArtwork();
