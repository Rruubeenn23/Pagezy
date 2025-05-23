document.addEventListener("DOMContentLoaded", () => {
  const track = document.querySelector(".slider-track");
  const slides = document.querySelectorAll(".slider-item");
  let currentIndex = 0;

  function nextSlide() {
    currentIndex = (currentIndex + 1) % slides.length;
    const offset = -currentIndex * 100;
    track.style.transform = `translateX(${offset}%)`;
  }

  setInterval(nextSlide, 3500);
});
