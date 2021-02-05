$(document).ready(function(){
    $(window).scroll(function(){
        if(this.scrollY > 20){
            $('.navbar').addClass('sticky');
        }else{
            $('.navbar').removeClass('sticky');
        }
        if(this.scrollY > 500){
            $('.scroll-up-btn').addClass('show');
        }else{
            $('.scroll-up-btn').removeClass('show');
        }
    });

    // scroll to top 
    $('.scroll-up-btn').click(function(){
        $('html').animate({scrollTop: 0});
    });


    // toogle navigation
    $('.menu-bars').click(function(){
        $('.navbar .menu').toggleClass("active");
        $('.menu-bars i').toggleClass("active");
    });

    // typing animation
    var typed = new Typed(".type-animate", {
        strings : ['fullstack web developer.','graphic designer.','python programmer.','Data analyst','freelancer'],
        typeSpeed : 100,
        backSpeed : 60,
        loop: true
    });

    var typed = new Typed(".type-animate-2", {
        strings : ['fullstack web developer.','graphic designer.','python programmer.','Data analyst','freelancer'],
        typeSpeed : 100,
        backSpeed : 60,
        loop: true
    });

    // carousel effect 

    $(".carousel").owlCarousel({
        margin: 20,
        loop: true,
        autoplay: true,
        autoplayTimeOut: 2000,
        autoplayHoverPause: true,
        responsive: {
            0:{
                items: 1,
                nav: false
            },
            600:{
                items: 2,
                nav: false
            },
            1000:{
                items: 3,
                nav: false
            }
        }
    });

    $(".play").on('click', function(){
        $('.owl-carousel').trigger('play.owl.autoplay', [1000])
    })
});


const myname = document.querySelectorAll('#myName path');
for(let i = 0; i < myname.length; i++) {
    console.log(i, myname[i].getTotalLength());
}

function showSkills(){
    document.getElementById('modal').style.display = 'block';
}

function closeSkills(){
    document.getElementById('modal').style.display = 'none';
}