
// Main entry point when the document is ready
document.addEventListener('DOMContentLoaded', function() {
    // Initialize all dynamic features
    initAnimations();
    initNavigation();
    initScrollEffects();
    initNewsletterForm();
});

// Animation initialization
function initAnimations() {
    // Fade in animations
    const fadeElements = document.querySelectorAll('.fade-in');
    
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    fadeElements.forEach(element => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(20px)';
        element.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(element);
    });
}

// Navigation functionality
function initNavigation() {
    // Dropdown functionality
    const dropdowns = document.querySelectorAll('.dropdown');
    
    dropdowns.forEach(dropdown => {
        const toggle = dropdown.querySelector('.dropdown-toggle');
        const menu = dropdown.querySelector('.dropdown-menu');
        
        if (toggle && menu) {
            // Handle hover for desktop
            dropdown.addEventListener('mouseenter', function() {
                menu.style.display = 'block';
            });
            
            dropdown.addEventListener('mouseleave', function() {
                menu.style.display = 'none';
            });
            
            // Handle click for mobile
            toggle.addEventListener('click', function(e) {
                e.preventDefault();
                if (window.innerWidth <= 768) {
                    menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
                }
            });
        }
    });
    
    // Close dropdowns when clicking outside
    document.addEventListener('click', function(e) {
        if (!e.target.closest('.dropdown')) {
            const dropdownMenus = document.querySelectorAll('.dropdown-menu');
            dropdownMenus.forEach(menu => {
                menu.style.display = 'none';
            });
        }
    });
}

// Scroll effects
function initScrollEffects() {
    let ticking = false;
    
    function updateScrollEffects() {
        const scrolled = window.pageYOffset;
        const rate = scrolled * -0.5;
        
        // Parallax effect for hero section
        const hero = document.querySelector('.hero-section');
        if (hero) {
            hero.style.transform = `translateY(${rate}px)`;
        }
        
        ticking = false;
    }
    
    function requestScrollUpdate() {
        if (!ticking) {
            requestAnimationFrame(updateScrollEffects);
            ticking = true;
        }
    }
    
    window.addEventListener('scroll', requestScrollUpdate);
}

// Smooth scrolling for anchor links
document.addEventListener('click', function(e) {
    if (e.target.matches('a[href^="#"]')) {
        e.preventDefault();
        const targetId = e.target.getAttribute('href').substring(1);
        const targetElement = document.getElementById(targetId);
        
        if (targetElement) {
            targetElement.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    }
});

// Newsletter form specific handling
function initNewsletterForm() {
    const newsletterForm = document.querySelector('.newsletter-form');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const emailInput = this.querySelector('input[type="email"]');
            const email = emailInput.value;
            const button = this.querySelector('button');
            const originalText = button.textContent;
            
            if (email) {
                button.textContent = 'Subscribing...';
                button.disabled = true;

                fetch('/subscribe', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json'
                    },
                    body: JSON.stringify({ email: email })
                })
                .then(response => response.json())
                .then(data => {
                    // A more elegant solution would be to create a small notification popup
                    // instead of using alert().
                    alert(data.message); 

                    if (data.success) {
                        button.textContent = 'Subscribed!';
                        button.style.background = '#27ae60'; // Success color
                        emailInput.value = '';
                    } else {
                        button.textContent = 'Failed';
                        button.style.background = '#e74c3c'; // Error color
                    }
                })
                .catch(error => {
                    console.error('Subscription error:', error);
                    alert('An error occurred. Please try again.');
                    button.textContent = 'Error';
                    button.style.background = '#e74c3c';
                })
                .finally(() => {
                    setTimeout(() => {
                        button.textContent = originalText;
                        button.style.background = '';
                        button.disabled = false;
                    }, 3000);
                });
            }
        });
    }
}

// Error handling
window.addEventListener('error', function(e) {
    console.warn('JavaScript error caught:', e.message);
    // Prevent errors from breaking the page
    return true;
});
