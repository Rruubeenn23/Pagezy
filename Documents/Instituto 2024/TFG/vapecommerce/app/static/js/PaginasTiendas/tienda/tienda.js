document.addEventListener("DOMContentLoaded", () => {
    const slider = document.querySelector(".slider-productos");
    const btnPrev = document.querySelector(".slider-btn-prev");
    const btnNext = document.querySelector(".slider-btn-next");
  
    if (!slider || !btnPrev || !btnNext) return;
  
    const scrollAmount = slider.querySelector(".tarjeta-producto")?.offsetWidth || 300;
  
    btnPrev.addEventListener("click", () => {
      slider.scrollBy({ left: -scrollAmount, behavior: "smooth" });
    });
  
    btnNext.addEventListener("click", () => {
      slider.scrollBy({ left: scrollAmount, behavior: "smooth" });
    });
  });