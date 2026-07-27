(function () {
    document.querySelectorAll('.search-bar input, .search-box input').forEach(input => {
        input.setAttribute('aria-label', 'Search artwork titles and tags');
        input.addEventListener('keydown', event => {
            if (event.key !== 'Enter') return;
            event.preventDefault();
            const query = input.value.trim();
            if (query) {
                window.location.href =
                    `Search.html?q=${encodeURIComponent(query)}&mode=all`;
            }
        });
    });
})();
