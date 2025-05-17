document.addEventListener("DOMContentLoaded", () => {
    // Toggle de carpetas
    const toggles = document.querySelectorAll(".toggle-carpeta");
    toggles.forEach(toggle => {
        toggle.addEventListener("click", () => {
            console.log("Carpeta clicada");
            const contenido = toggle.closest(".carpeta").querySelector(".contenido-carpeta");
            contenido.classList.toggle("abierta");
            toggle.textContent = contenido.classList.contains("abierta") ? "Ocultar" : "Mostrar";
          });          
    });
  
    // Seleccionar todos los productos
    const selectAll = document.getElementById("select-all");
    const allProductChecks = document.querySelectorAll(".checkbox-vaper");
  
    selectAll.addEventListener("change", () => {
      allProductChecks.forEach(checkbox => {
        checkbox.checked = selectAll.checked;
      });
      document.querySelectorAll(".select-tipo").forEach(tipoCheck => {
        tipoCheck.checked = selectAll.checked;
      });
    });
  
    // Seleccionar todos los productos de un tipo
    const tipoChecks = document.querySelectorAll(".select-tipo");
    tipoChecks.forEach(tipoCheck => {
      tipoCheck.addEventListener("change", () => {
        const tipo = tipoCheck.dataset.tipo;
        document.querySelectorAll(`.checkbox-vaper[data-tipo="${tipo}"]`)
          .forEach(cb => cb.checked = tipoCheck.checked);
      });
    });
  
    // Si desmarcas uno, desmarca el tipo y el global
    allProductChecks.forEach(checkbox => {
      checkbox.addEventListener("change", () => {
        const tipo = checkbox.dataset.tipo;
  
        const todosTipo = document.querySelectorAll(`.checkbox-vaper[data-tipo="${tipo}"]`);
        const checkTipo = document.querySelector(`.select-tipo[data-tipo="${tipo}"]`);
        checkTipo.checked = [...todosTipo].every(cb => cb.checked);
  
        selectAll.checked = [...allProductChecks].every(cb => cb.checked);
      });
    });
  });
  