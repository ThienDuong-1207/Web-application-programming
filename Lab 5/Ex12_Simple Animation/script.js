const box = document.getElementById("box");
let position = 0;
const interval = setInterval(
    () => {
        position += 1;
        box.style.left = position + "px";
        if (position >= 1000) clearInterval(interval);
    }, 20
);