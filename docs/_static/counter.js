document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".highlight pre").forEach((pre) => {
        const lines = pre.innerHTML.split("\n");

        if (lines.length && lines[lines.length - 1].trim() === "") {
            lines.pop();
        }

        pre.innerHTML = lines
            .map(line => `<span class="code-line">${line}</span>`)
            .join("\n");
    });
});