const track = document.querySelector(".carousel__track");
const slides = Array.from(track.children);
const nextBtn = document.querySelector(".carousel__btn--right");
const prevBtn = document.querySelector(".carousel__btn--left");
const dotsNav = document.querySelector(".carousel__nav");
const dots = Array.from(dotsNav.children);

const slideWidth = slides[0].getBoundingClientRect().width;

const setSlidePosition = (slide, index) => {
    slide.style.left = (slideWidth + slideWidth * (10 / 100)) * index + "px";
};
slides.forEach(setSlidePosition);

const moveToSlide = (track, currentSlide, targetSlide) => {
    track.style.transform = "translateX(-" + targetSlide.style.left + ")";
    currentSlide.classList.remove("current-slide");
    targetSlide.classList.add("current-slide");
};

const updateDots = (currentDot, targetDot) => {
    currentDot.classList.remove("current-slide");
    targetDot.classList.add("current-slide");
};

prevBtn.addEventListener("click", (e) => {
    const currentSlide = track.querySelector(".current-slide");
    const currentDot = dotsNav.querySelector(".current-slide");
    let { prevSlide, prevDot } = "";

    if (currentSlide.previousElementSibling) {
        prevSlide = currentSlide.previousElementSibling;
        prevDot = currentDot.previousElementSibling;
    } else {
        prevSlide = slides[slides.length - 1];
        prevDot = dots[dots.length - 1];
    }
    moveToSlide(track, currentSlide, prevSlide);
    updateDots(currentDot, prevDot);
});

nextBtn.addEventListener("click", (e) => {
    const currentSlide = track.querySelector(".current-slide");
    const currentDot = dotsNav.querySelector(".current-slide");
    let { nextSlide, nextDot } = "";

    if (currentSlide.nextElementSibling) {
        nextSlide = currentSlide.nextElementSibling;
        nextDot = currentDot.nextElementSibling;
    } else {
        nextSlide = slides[0];
        nextDot = dots[0];
    }
    moveToSlide(track, currentSlide, nextSlide);
    updateDots(currentDot, nextDot);
});

dotsNav.addEventListener("click", (e) => {
    const targetDot = e.target.closest("button");
    if (!targetDot) return;

    const currentSlide = track.querySelector(".current-slide");
    const currentDot = dotsNav.querySelector(".current-slide");
    const targetIndex = dots.findIndex((dots) => dots === targetDot);
    const targetSlide = slides[targetIndex];

    moveToSlide(track, currentSlide, targetSlide);
    updateDots(currentDot, targetDot);
});

document.addEventListener("DOMContentLoaded", function () {
    setInterval(() => nextBtn.click(), 5000);
});
