document.addEventListener('DOMContentLoaded', function() {
    // Media filtering functionality
    const filterBtns = document.querySelectorAll('.media-filters .filter-btn');
    const mediaCards = document.querySelectorAll('.media-card');
    
    filterBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            // Remove active class from all buttons
            filterBtns.forEach(b => b.classList.remove('active'));
            // Add active class to clicked button
            this.classList.add('active');
            
            const filter = this.getAttribute('data-filter');
            
            mediaCards.forEach(card => {
                if (filter === 'all' || card.getAttribute('data-type') === filter) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });
    
    // Video modal functionality
    const modal = document.getElementById('videoModal');
    const videoFrame = document.getElementById('videoFrame');
    const closeBtn = document.querySelector('.modal .close');
    const watchBtns = document.querySelectorAll('.watch-btn');
    
    watchBtns.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const videoUrl = this.getAttribute('data-video');
            videoFrame.src = videoUrl;
            modal.style.display = 'block';
        });
    });
    
    const closeModal = () => {
        modal.style.display = 'none';
        videoFrame.src = ''; // Stop video playback
    };

    closeBtn.addEventListener('click', closeModal);
    window.addEventListener('click', (e) => e.target === modal && closeModal());
});