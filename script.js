// Probiz script.js

document.addEventListener('DOMContentLoaded', () => {

    // 1. Sticky Glass Header
    const header = document.getElementById('header');
    window.addEventListener('scroll', () => {
        if (header) {
            if (window.scrollY > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        }
    });

    // 2. Mobile Nav Toggle
    const hamburger = document.getElementById('hamburger');
    const navMenu = document.querySelector('.nav-menu');

    if (hamburger && navMenu) {
        hamburger.addEventListener('click', () => {
            navMenu.classList.toggle('active');
            hamburger.classList.toggle('active');
            const bars = hamburger.querySelectorAll('.bar');
            if (hamburger.classList.contains('active')) {
                bars[0].style.transform = 'translateY(8px) rotate(45deg)';
                bars[1].style.opacity = '0';
                bars[2].style.transform = 'translateY(-8px) rotate(-45deg)';
            } else {
                bars[0].style.transform = 'translateY(0) rotate(0)';
                bars[1].style.opacity = '1';
                bars[2].style.transform = 'translateY(0) rotate(0)';
            }
        });

        document.querySelectorAll('.nav-link').forEach(n => n.addEventListener('click', () => {
            navMenu.classList.remove('active');
            hamburger.classList.remove('active');
            const bars = hamburger.querySelectorAll('.bar');
            if (bars.length >= 3) {
                bars[0].style.transform = 'translateY(0) rotate(0)';
                bars[1].style.opacity = '1';
                bars[2].style.transform = 'translateY(0) rotate(0)';
            }
        }));
    }

    // 3. Parallax Hero Image
    const parallaxEl = document.querySelector('.hero-video-wrap img');
    window.addEventListener('scroll', () => {
        if (parallaxEl && window.scrollY < window.innerHeight) {
            parallaxEl.style.transform = `translateY(${window.scrollY * 0.3}px) scale(1.05)`;
        }
    });

    // 4. Intersection Observer — Staggered Reveal
    const revealElements = document.querySelectorAll('.reveal, .fade-in');
    const revealOnScroll = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (!entry.isIntersecting) return;
            entry.target.classList.add('active');
            observer.unobserve(entry.target);
        });
    }, { threshold: 0.08, rootMargin: '0px 0px -30px 0px' });

    revealElements.forEach(el => {
        const rect = el.getBoundingClientRect();
        const inViewport = rect.top < window.innerHeight && rect.bottom > 0;
        if (!inViewport) el.classList.add('animate-ready');
        revealOnScroll.observe(el);
    });

    // 5. Card Tilt Effect
    const tiltCards = document.querySelectorAll('.glass-card, .feature-img-box, .metric-card');
    tiltCards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const xNorm = ((e.clientX - rect.left) / rect.width - 0.5) * 2;
            const yNorm = ((e.clientY - rect.top) / rect.height - 0.5) * -2;
            card.style.transform = `perspective(1000px) rotateX(${yNorm * 6}deg) rotateY(${xNorm * 6}deg) translateY(-8px) scale(1.02)`;
        });
        card.addEventListener('mouseleave', () => {
            card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0) scale(1)';
        });
    });

    // 6. Language Selector
    const langSelector = document.getElementById('langSelector');
    const langBtn = document.getElementById('langBtn');
    const langLabel = document.getElementById('langLabel');
    const langFlag = document.getElementById('langFlag');

    if (langBtn && langSelector) {
        const saved = localStorage.getItem('probiz_lang') || 'en';
        
        // Initial set
        setTimeout(() => {
            setLanguage(saved);
        }, 50);

        langBtn.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            langSelector.classList.toggle('open');
        });

        document.addEventListener('click', (e) => {
            if (!langSelector.contains(e.target)) {
                langSelector.classList.remove('open');
            }
        });

        document.querySelectorAll('.lang-option').forEach(opt => {
            opt.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                const lang = opt.dataset.lang;
                if (lang) {
                    setLanguage(lang);
                    localStorage.setItem('probiz_lang', lang);
                    langSelector.classList.remove('open');
                }
            });
        });
    }

    function setLanguage(code) {
        const langConfigs = {
            en: { label: 'EN', flag: '🇬🇧', dir: 'ltr' },
            ar: { label: 'AR', flag: '🇦🇪', dir: 'rtl' },
            fr: { label: 'FR', flag: '🇫🇷', dir: 'ltr' },
            de: { label: 'DE', flag: '🇩🇪', dir: 'ltr' },
            es: { label: 'ES', flag: '🇪🇸', dir: 'ltr' }
        };
        const cfg = langConfigs[code] || langConfigs['en'];
        
        if (langLabel) langLabel.textContent = cfg.label;
        if (langFlag) langFlag.textContent = cfg.flag;
        
        document.documentElement.lang = code;
        document.documentElement.dir = cfg.dir;
        
        document.querySelectorAll('.lang-option').forEach(opt => {
            opt.classList.toggle('active', opt.dataset.lang === code);
        });
        
        applyTranslations(code);
    }

    // 7. Dynamic Translation Engine
    if (!window.PROBIZ_DATA) {
        window.PROBIZ_DATA = {
            originalHTML: new Map()
        };
    }

    function applyTranslations(targetLang) {
        if (typeof translations === 'undefined') {
            console.warn("Translations object missing.");
            return;
        }

        const dict = translations[targetLang];
        
        document.querySelectorAll('[data-i18n]').forEach(el => {
            const key = el.getAttribute('data-i18n');
            
            if (!window.PROBIZ_DATA.originalHTML.has(el)) {
                window.PROBIZ_DATA.originalHTML.set(el, el.innerHTML);
            }

            if (targetLang === 'en' || !dict || !dict[key]) {
                el.innerHTML = window.PROBIZ_DATA.originalHTML.get(el);
            } else {
                el.innerHTML = dict[key];
            }
        });
    }

});
