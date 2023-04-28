$('.heading').click(function () {
    $(this).toggleClass('active').next('.cont_hide').slideToggle();
    $(this).parent('').siblings().children('.heading').removeClass('active').next('.cont_hide').slideUp();
    });

    $(window).scroll(function () {
        var scroll = $(window).scrollTop();
        if (scroll >= 50) {
            $("header").addClass("top-fixed");
        } else {
            $("header").removeClass("top-fixed");
        }
    });
