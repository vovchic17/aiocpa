document.addEventListener("DOMContentLoaded", () => {
  const copyright = document.querySelector(".copyright");

  if (!copyright) {
    return;
  }

  const year = copyright.textContent
    .replace("Copyright ©", "")
    .trim();

  copyright.innerHTML = `
        Copyright © ${year}<br>
        Developed by <a href="https://github.com/vovchic17" target="_blank" rel="noopener noreferrer">vovchic17</a><br>
        Designed by <a href="https://t.me/nastazzzydesign" target="_blank" rel="noopener noreferrer">nastazzzy</a>
    `;
});