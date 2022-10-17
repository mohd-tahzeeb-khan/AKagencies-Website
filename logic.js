//Navbar for mobile Views

const mobile_nav=document.querySelector(" .mobilenavbar-button");
const nav_header=document.querySelector(".header");
const toggleNavbar=()=>{
    nav_header.classList.toggle("active");
}
mobile_nav.addEventListener("click", ()=> toggleNavbar());
// Animation of Rating Section 

const ratingsection = document.querySelector(".rating-section");
const ratingobserve= new IntersectionObserver((entries, observer)=>{
    const [entry]=entries;
    if(!entry.isIntersecting) return;
    const counternumber =document.querySelectorAll(".rating");
    const speed=200;
    counternumber.forEach(element => {
        const updatenumber=() =>{
            const targetnumber=parseInt(element.dataset.number);
           // console.log(targetnumber);
            const intialNum = parseInt(element.innerText);
            //console.log(intialNum)

            const incrementNumber = Math.trunc(targetnumber/speed);
            //console.log(incrementNumber)
            if (intialNum<targetnumber){
                element.innerText=(intialNum + incrementNumber);
                setTimeout(updatenumber, 10);
            }

    };
    updatenumber();
});
observer.unobserve(ratingsection)
}, {
    root:null,
    theshold:0,
});
ratingobserve.observe(ratingsection)

//Testimonials Section-------------------
new Swiper(".mySwiper", {
    slidesPerView: 3,
    spaceBetween: 30,
    autoplay:{
        delay:2500,
        disableOnInteraction:false,
    },
    freeMode: true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
  });

const Testimonialsmediaquery =(widthsize) =>{
    if (widthsize.matches){
        new Swiper(".mySwiper", {
            slidesPerView: 1,
    spaceBetween: 10,
    autoplay:{
        delay:2500,
        disableOnInteraction:false,
    },
    freeMode: true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    }
            });
    }
    else{
        new Swiper(".mySwiper", {
            slidesPerView: 3,
            spaceBetween: 30,
          });
        }
};
const widthsize= window.matchMedia("(max-width: 780px)");
Testimonialsmediaquery(widthsize);
widthsize.addEventListener('change', Testimonialsmediaquery);


//var swiper = new Swiper(".mySwiper", {
//    slidesPerView: 3,
//    spaceBetween: 30,
//    autoplay:{
//        delay:2500,
//    },
//    freeMode: true,
//    pagination: {
//      el: ".swiper-pagination",
//      clickable: true,
//    },
//  });


 //Brands automation
var swiper = new Swiper(".mySwiper-brand", {
    slidesPerView: 3,
    spaceBetween: 30,
    loop:true,
    autoplay:{
        delay:1500,
    },
    freeMode: true,
  });

  const Partnersmediaquery =(widthsizepartner) =>{
    if (widthsizepartner.matches){
        new Swiper(".mySwiper-brand", {
            slidesPerView: 3,
            spaceBetween:100,
            });
    }
    else{
        new Swiper(".mySwiper-brand", {
            slidesPerView: 3,
            spaceBetween: 30,
          });
        }
};
const widthsizepartner= window.matchMedia("(max-width: 780px)");
Partnersmediaquery(widthsizepartner);
widthsizepartner.addEventListener('change', Partnersmediaquery);