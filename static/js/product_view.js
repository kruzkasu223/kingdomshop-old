let thumbnails = document.getElementsByClassName("thumbnail");
let activeImage = document.getElementsByClassName("active");

for (let i = 0; i < thumbnails.length; i++) {
    thumbnails[i].addEventListener("mouseover", function () {
        if (activeImage.length > 0) {
            activeImage[0].classList.remove("active");
        }
        this.classList.add("active");
        document.getElementById("featured_img").src = this.src;
    });
    thumbnails[i].addEventListener("click", function () {
        if (activeImage.length > 0) {
            activeImage[0].classList.remove("active");
        }
        this.classList.add("active");
        document.getElementById("featured_img").src = this.src;
    });
}

let buttonLeft = document.getElementById("buttonLeft");
let buttonRight = document.getElementById("buttonRight");

buttonLeft.addEventListener("click", function () {
    document.getElementById("slider").scrollLeft -= 150;
});

buttonRight.addEventListener("click", function () {
    document.getElementById("slider").scrollLeft += 150;
});

function scrollReview() {
    document.getElementById("reviews").scrollIntoView({
        block: "center",
        behavior: "smooth",
    });
}
