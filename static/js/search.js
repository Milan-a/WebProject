document.addEventListener('DOMContentLoaded', function() {
    const searchLink = document.getElementById('searchLink');

    if (searchLink) {
        searchLink.addEventListener('click', function(event) {
            event.preventDefault();

            const categorySelect = document.getElementById('categorySelect');
            const searchInput = document.getElementById('searchInput');

            const categoryValue = categorySelect.value;
            const requestValue = searchInput.value;

            const basePath = this.dataset.basePath;
            const defaultPath = this.dataset.defaultPath;

            if (!requestValue.trim()) {
                window.location.href = defaultPath;
                return;
            }

            const finalUrl = `${basePath}/${encodeURIComponent(categoryValue)}/${encodeURIComponent(requestValue)}`;
            window.location.href = finalUrl;
        });
    }
});