$(document).ready(function () {
    $(window).scroll(function (e) {
        // add/remove class to navbar when scrolling to hide/show
        e.preventDefault();

        $(".navbar")[$(window).scrollTop() >= 150 ? "addClass" : "removeClass"](
            "navbar-hide"
        );
    });

    var $win = $(window);
    var $stat = $(".animation"); // Change this to affect your desired element.

    $win.on("scroll", function () {
        var scrollTop = $win.scrollTop();

        $stat.each(function () {
            var $self = $(this);
            var prev = $self.offset();
            if (scrollTop - prev.top > -500 && $(window).width() > 576) {
                $self.css("opacity", "1");
                $(this)
                    .find($(".animation_left"))
                    .addClass("animate__animated animate__fadeInLeft");
                $(this)
                    .find($(".animation_right"))
                    .addClass("animate__animated animate__fadeInRight");
                $(this)
                    .find($(".animation_top"))
                    .addClass("animate__animated animate__fadeInUp");
            }
            else if($(window).width() < 576 && scrollTop - prev.top > -750){
                $self.css("opacity", "1");
                $(this)
                    .find($(".animation_left"))
                    .addClass("animate__animated animate__fadeIn");
                $(this)
                    .find($(".animation_right"))
                    .addClass("animate__animated animate__fadeIn");
                $(this)
                    .find($(".animation_top"))
                    .addClass("animate__animated animate__fadeIn");
            }
            else{
            }
        });
    }).scroll();

    $(
        (function ($, win) {
            $.fn.inViewport = function (cb) {
                return this.each(function (i, el) {
                    function visPx() {
                        var H = $(this).height(),
                            r = el.getBoundingClientRect(),
                            t = r.top,
                            b = r.bottom;
                        return cb.call(
                            el,
                            Math.max(0, t > 0 ? H - t : b < H ? b : H)
                        );
                    }
                    visPx();
                    $(win).on("resize scroll", visPx);
                });
            };
        })(jQuery, window)
    );

    jQuery(function ($) {
        // DOM ready and $ in scope

        $(".counter-number").inViewport(function (px) {
            // Make use of the `px` argument!!!
            // if element entered V.port ( px>0 ) and
            // if prop initNumAnim flag is not yet set
            //  = Animate numbers
            if (px > 0 && !this.initNumAnim) {
                this.initNumAnim = true; // Set flag to true to prevent re-running the same animation
                $(this)
                    .prop("Counter", 0)
                    .animate(
                        {
                            Counter: $(this).text(),
                        },
                        {
                            duration: 1000,
                            step: function (now) {
                                $(this).text(Math.ceil(now));
                            },
                        }
                    );
            }
        });
    });
});

$(document).ready(function () {
    $(window).one("scroll", function () {
        $("video").each(function () {
            if ($(this).is(":in-viewport(0)")) {
                $(this)[0].play();
            } else {
                $(this)[0].pause();
            }
        });
    });
});

$(document).ready(function () {
    $(".owl-carousel").owlCarousel({
        items: 3,
        loop: true,
        autoplay: true,
        margin: 20,
        autoplayTimeout: 4000,
        autoplayHoverPause: true,
        stagePadding: 50,
        dots: false,
        responsive: {
            0: {
                items: 1,
            },
            500: {
                items: 1,
            },
            700: {
                items: 2,
            },
            1000: {
                items: 3,
            },
            1200: {
                items: 5,
            },
        },
    });
    $(".search-icon").click(function () {
        $(".search-bar").fadeIn();
    });
    $(".close-btn").click(function () {
        $(".search-bar").fadeOut();
    });
});
