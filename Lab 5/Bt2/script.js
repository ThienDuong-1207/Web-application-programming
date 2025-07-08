const images = [
    "images/1.jpg",
    "images/2.jpg",
    "images/3.jpg",
];

let currentIndex = 0;
const slide = document.getElementById("slide");

function showImage(i) {
    currentIndex = (i + images.length) % images.length; // Ensure index wraps around
    slide.src = images[currentIndex];
}

function nextSlide() {
  showImage(currentIndex + 1);
}

function prevSlide() {
  showImage(currentIndex - 1);
}

setInterval(() => nextSlide(), 3000);