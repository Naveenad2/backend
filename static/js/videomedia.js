document.addEventListener('DOMContentLoaded', () => {
    const loadMoreButton = document.getElementById('load-more');

    loadMoreButton?.addEventListener('click', () => {
        const offset = parseInt(loadMoreButton.getAttribute('data-offset'), 10);

        fetch(`/load-more-media/?offset=${offset}`)
            .then(response => response.json())
            .then(data => {
                const mediaSection = document.getElementById('media-container');

                data.media_items.forEach((itemData, index) => {
                    const col = document.createElement('div');
                    col.classList.add('col-md-6', 'mb-4');

                    const mediaItem = document.createElement('div');
                    mediaItem.classList.add('media-item', 'border', 'border-warning', 'p-3');

                    if (itemData.media_type === 'local') {
                        const video = document.createElement('video');
                        video.classList.add('img-fluid');
                        video.controls = true;

                        const source = document.createElement('source');
                        source.src = itemData.video_file;
                        source.type = 'video/mp4';

                        video.appendChild(source);
                        mediaItem.appendChild(video);
                    } else if (itemData.media_type === 'youtube') {
                        const iframe = document.createElement('iframe');
                        iframe.classList.add('img-fluid');
                        iframe.src = `https://www.youtube.com/embed/${itemData.video_url}`;
                        iframe.frameborder = 0;
                        iframe.allow = 'accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture';
                        iframe.allowFullscreen = true;

                        mediaItem.appendChild(iframe);
                    }

                    const description = document.createElement('div');
                    description.classList.add('media-description', 'mt-2');
                    description.textContent = itemData.description;

                    mediaItem.appendChild(description);
                    col.appendChild(mediaItem);
                    mediaSection.appendChild(col);
                });

                // Update offset for the next batch
                const newOffset = offset + data.media_items.length;
                loadMoreButton.setAttribute('data-offset', newOffset);

                // Hide the load more button if no more items to load
                if (data.media_items.length < 8) {
                    loadMoreButton.style.display = 'none';
                }
            });
    });
});
