export function actualizarProgreso(pasoActual) {
  const etiquetaPaso = document.getElementById("etiqueta-paso");
  const barraProgreso = document.getElementById("progreso");

  if (!etiquetaPaso || !barraProgreso) return;

  const porcentajes = {
      1: "25, 100",
      2: "50, 100",
      3: "75, 100",
      4: "100, 100"
  };

  etiquetaPaso.textContent = pasoActual;
  barraProgreso.setAttribute("stroke-dasharray", porcentajes[pasoActual] || "0, 100");
}
