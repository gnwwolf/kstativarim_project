// Анимации при скролле
document.addEventListener('DOMContentLoaded', function() {
    // Анимация появления элементов
    const animateElements = document.querySelectorAll('.feature-card, .service-card, .gallery-item');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });
    animateElements.forEach(el => observer.observe(el));
    // Автоматическое закрытие сообщений через 5 секунд
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.classList.add('fade');
            setTimeout(() => alert.remove(), 500);
        }, 5000);
    });
});
// Функция для полноэкранного просмотра изображений
function openFullscreen(img) {
    const modal = document.getElementById('fullscreenModal');
    const fullscreenImg = document.getElementById('fullscreenImage');
    const caption = document.getElementById('fullscreenCaption');
    
    if (modal && fullscreenImg) {
        fullscreenImg.src = img.src;
        if (caption && img.alt) {
            caption.innerHTML = `<h3>${img.alt}</h3>`;
        }
        modal.style.display = 'block';
    }
}
function closeFullscreen() {
    const modal = document.getElementById('fullscreenModal');
    if (modal) {
        modal.style.display = 'none';
    }
}
// Закрытие по ESC
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        closeFullscreen();
    }
});