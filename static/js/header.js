var menuBtn = document.querySelector(".menu_btn");
var menuBar1 = document.querySelector("#menu_btn_bar_1");
var menuBar2 = document.querySelector("#menu_btn_bar_2");
var menuBar3 = document.querySelector("#menu_btn_bar_3");
var navMenu = document.querySelector(".nav_menu_div");

menuBtn.addEventListener("click", () => {
    menuBar2.classList.toggle("hidden_block");
    menuBar1.classList.toggle("rotate_1");
    menuBar3.classList.toggle("rotate_2");
    navMenu.classList.toggle("visible_block");
});

window.addEventListener("click", (e) => {
    if (e.target == navMenu) {
        navMenu.classList.toggle("visible_block");
        menuBar2.classList.toggle("hidden_block");
        menuBar1.classList.toggle("rotate_1");
        menuBar3.classList.toggle("rotate_2");
    }
});
