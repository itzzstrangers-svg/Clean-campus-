// ===============================
// Clean Campus Reporting Website
// script.js
// ===============================

// Mobile Menu (if added later)
const menuBtn = document.querySelector(".menu-btn");
const navLinks = document.querySelector(".navbar ul");

if(menuBtn){
    menuBtn.addEventListener("click", () => {
        navLinks.classList.toggle("show");
    });
}

// Navbar Background Change on Scroll
window.addEventListener("scroll", () => {

    const navbar = document.querySelector(".navbar");

    if(window.scrollY > 50){
        navbar.style.background = "rgba(0,0,0,0.9)";
        navbar.style.transition = "0.4s";
    }else{
        navbar.style.background = "rgba(255,255,255,0.08)";
    }

});

// Smooth Scrolling
document.querySelectorAll('a').forEach(link => {

    link.addEventListener("click", function(e){

        const href = this.getAttribute("href");

        if(href.startsWith("#")){

            e.preventDefault();

            document.querySelector(href).scrollIntoView({

                behavior:"smooth"

            });

        }

    });

});

// 3D Card Hover Effect
const cards = document.querySelectorAll(".card");

cards.forEach(card=>{

    card.addEventListener("mouseenter",()=>{

        card.style.transform="translateY(-10px) scale(1.05)";

    });

    card.addEventListener("mouseleave",()=>{

        card.style.transform="translateY(0) scale(1)";

    });

});

// Welcome Message
window.onload = ()=>{

    console.log("Welcome to Clean Campus Reporting Website");

};

// Footer Year
const footer = document.querySelector("footer p");

if(footer){

    footer.innerHTML =
    "© " + new Date().getFullYear() +
    " Clean Campus Reporting Website | All Rights Reserved";

}