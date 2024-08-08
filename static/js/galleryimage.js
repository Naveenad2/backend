document.addEventListener('DOMContentLoaded', () => {
    const loadMoreButton = document.getElementById('load-more');

    loadMoreButton?.addEventListener('click', () => {
        const offset = parseInt(loadMoreButton.getAttribute('data-offset'), 10);

        fetch(`/load-more-images/?offset=${offset}`)
            .then(response => response.json())
            .then(data => {
                const gallery = document.querySelector('.gallery-section .row');

                data.images.forEach((imageData, index) => {
                    const col = document.createElement('div');
                    col.classList.add('col-md-4', 'mb-4');

                    const galleryItem = document.createElement('div');
                    galleryItem.classList.add('gallery-item');

                    const img = document.createElement('img');
                    img.src = imageData.src;
                    img.alt = imageData.alt;
                    img.classList.add('img-fluid');

                    const description = document.createElement('div');
                    description.classList.add('gallery-description');
                    description.style.display = 'none';
                    description.textContent = imageData.description;

                    galleryItem.appendChild(img);
                    galleryItem.appendChild(description);
                    col.appendChild(galleryItem);
                    gallery.appendChild(col);

                    // Add click event for enlarging image
                    addImageClickEvent(img, description);
                });

                // Update offset for the next batch
                const newOffset = offset + data.images.length;
                loadMoreButton.setAttribute('data-offset', newOffset);

                // Hide the load more button if no more images to load
                if (data.images.length < 12) {
                    loadMoreButton.style.display = 'none';
                }
            });
    });

    // Enlarge image on click for existing images
    document.querySelectorAll('.gallery-item img').forEach(img => {
        const description = img.nextElementSibling;
        addImageClickEvent(img, description);
    });
});

// Function to handle image click event
function addImageClickEvent(img, description) {
    img.addEventListener('click', () => {
        const modal = document.createElement('div');
        modal.classList.add('modal');
        modal.innerHTML = `
            <span class="close">&times;</span>
            <img class="modal-content" id="img01">
            <div id="caption"></div>
        `;
        document.body.appendChild(modal);

        const modalImg = document.getElementById("img01");
        const captionText = document.getElementById("caption");

        modal.style.display = "block";
        modalImg.src = img.src;
        captionText.innerHTML = description.innerHTML;

        const closeModal = () => {
            modal.style.display = "none";
            modal.remove();
        };

        modal.querySelector('.close').addEventListener('click', closeModal);
        modal.addEventListener('click', e => {
            if (e.target === modal) {
                closeModal();
            }
        });
    });
}
