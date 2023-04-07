// Выбираем все элементы, которые нужно анимировать
const rectangles = document.querySelectorAll('.rectangle');

// Создаем экземпляр Intersection Observer
const observer = new IntersectionObserver((entries, observer) => {
  entries.forEach(entry => {
    // Если элемент видимый на экране, добавляем класс "fade-in"
    if (entry.isIntersecting) {
      entry.target.classList.add('fade-in');
      // Отключаем наблюдение за элементом, после того, как класс добавлен
      observer.unobserve(entry.target);
    }
  });
});

// Добавляем каждый прямоугольник в Intersection Observer
rectangles.forEach(rectangle => {
  observer.observe(rectangle);
});