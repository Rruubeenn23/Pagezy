import { actualizarProgreso } from './componentes/progreso.js';

document.addEventListener("DOMContentLoaded", () => {
  const paso = parseInt(document.body.dataset.paso || "1");
  actualizarProgreso(paso);
});

import './componentes/paso3.js';  // solo con importarlo, se ejecuta automáticamente
