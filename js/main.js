// Main JavaScript for RL Journey Website

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Add animation on scroll
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe algorithm cards
document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.algorithm-card, .philosophy-item');

    cards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(card);
    });

    // Add active class to current page in navigation
    const currentPath = window.location.pathname;
    document.querySelectorAll('nav a').forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
});

// Console message
console.log('%c🎯 Reinforcement Learning Journey', 'color: #2563eb; font-size: 20px; font-weight: bold;');
console.log('%cBuilt with PyScript, Prism.js, and curiosity', 'color: #7c3aed; font-size: 14px;');
console.log('%cExplore the code: https://github.com/yourusername/Reinforcement-Learning', 'color: #10b981;');
