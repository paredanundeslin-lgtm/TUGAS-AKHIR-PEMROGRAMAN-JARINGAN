document.addEventListener('DOMContentLoaded', () => {
    // Mobile Navigation Toggle
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const navLinks = document.getElementById('nav-links');

    if (mobileMenuBtn && navLinks) {
        mobileMenuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });

        // Close menu when clicking a link
        document.querySelectorAll('.nav-links a').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('active');
            });
        });
    }

    // Smooth Scrolling for Anchor Links (Backup for CSS scroll-behavior)
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Contact Form Simulation
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            // Simulate sending
            const btn = contactForm.querySelector('button[type="submit"]');
            const originalText = btn.innerText;

            btn.innerText = 'Mengirim...';
            btn.disabled = true;

            setTimeout(() => {
                alert('Terima kasih! Pesan Anda telah "terkirim" (demo).');
                contactForm.reset();
                btn.innerText = 'Terkirim!';

                setTimeout(() => {
                    btn.innerText = originalText;
                    btn.disabled = false;
                }, 2000);
            }, 1000);
        });
    }

    // Typing Effect for Hero
    const heroTitle = document.querySelector('.hero h1');
    if (heroTitle) {
        // Simple typing cursor effect could be added here if requested, 
        // but the CSS gradient text is already applied.
        // Let's add a subtitle typing effect instead if desired, or just leave the fancy CSS.
        // For now, the CSS gradient animation on h1 is sufficient "add animation."
    }

    // Advanced Scroll Reveal Animation
    const observerOptions = {
        threshold: 0.15,
        rootMargin: "0px 0px -50px 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target); // Only animate once
            }
        });
    }, observerOptions);

    // Elements to animate
    const revealElements = document.querySelectorAll('.section-title, .profile-text, .profile-img, .card, .article-item, .contact-form, .skill-card');

    revealElements.forEach((el, index) => {
        el.classList.add('reveal');

        // Add staggered delays for grids
        if (el.classList.contains('card') || el.classList.contains('article-item') || el.classList.contains('skill-card')) {
            // Calculate delay based on index in parent, simplified approach:
            // Just random or cycling delays for a natural feel
            // This simple modulo approach staggers items in a row (assuming 3 per row max usually)
            const delayClass = `delay-${((index % 5) + 1) * 100}`;
            el.classList.add(delayClass);
        }

        observer.observe(el);
    });


    // --- 3D Tilt Effect ---
    const tiltElements = document.querySelectorAll('.card, .skill-card');

    tiltElements.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            const centerX = rect.width / 2;
            const centerY = rect.height / 2;

            const rotateX = ((y - centerY) / centerY) * -10; // Max rotation deg
            const rotateY = ((x - centerX) / centerX) * 10;

            card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.05)`;
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) scale(1)';
        });
    });
});
