document.addEventListener('DOMContentLoaded', function () {
    function animateCount(id, endValue) {
        let element = document.getElementById(id);
        let startValue = 0;
        let duration = 2000; // 2 seconds
        let increment = endValue / (duration / 20); // update every 20ms
        let currentValue = startValue;
        let step = function () {
            currentValue += increment;
            if (currentValue < endValue) {
                element.innerText = Math.ceil(currentValue);
                requestAnimationFrame(step);
            } else {
                element.innerText = endValue;
            }
        };
        step();
    }

    function startCounting() {
        animateCount('clients-count', parseInt(document.getElementById('clients-count').innerText));
        animateCount('projects-count', parseInt(document.getElementById('projects-count').innerText));
        animateCount('upcoming-projects-count', parseInt(document.getElementById('upcoming-projects-count').innerText));
        animateCount('events-count', parseInt(document.getElementById('events-count').innerText));
    }

    let statsSection = document.querySelector('.stats');

    let options = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    let observer = new IntersectionObserver(function (entries, observer) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                startCounting();
                observer.unobserve(entry.target); // Stop observing after animation starts
            }
        });
    }, options);

    observer.observe(statsSection);
});
