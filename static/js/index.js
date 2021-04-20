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













$(document).ready(function(){
    $(".gallery-more.all-images a").click(function(){
        const i = parseInt($(this).attr("data-count"));
        const carouselItems = $(".gallery-more .carousel .carousel-item");
        carouselItems.each(function (idx) {
            if(i === idx){
                $(this).addClass("active");
            } else{
                $(this).removeClass("active");
            }
        });
    });

    $("#languageSelect").change(function () {
        $("#languageForm").submit();
    });
    // zoomImage();


    crear_select();
});

function isMobileDevice() {
    return (typeof window.orientation !== "undefined") || (navigator.userAgent.indexOf('IEMobile') !== -1);
};


var li = new Array();
function crear_select(){
    var div_cont_select = document.querySelectorAll("[data-mate-select='active']");
    var select_ = '';
    for (var e = 0; e < div_cont_select.length; e++) {
        div_cont_select[e].setAttribute('data-indx-select',e);
        div_cont_select[e].setAttribute('data-selec-open','false');
        var ul_cont = document.querySelectorAll("[data-indx-select='"+e+"'] > .cont_list_select_mate > ul");
        select_ = document.querySelectorAll("[data-indx-select='"+e+"'] >select")[0];
        if (isMobileDevice()) {
            select_.addEventListener('change', function () {
                _select_option(select_.selectedIndex,e);
            });
        }
        var select_optiones = select_.options;
        document.querySelectorAll("[data-indx-select='"+e+"']  > .selecionado_opcion ")[0].setAttribute('data-n-select',e);
        document.querySelectorAll("[data-indx-select='"+e+"']  > .icon_select_mate ")[0].setAttribute('data-n-select',e);
        for (var i = 0; i < select_optiones.length; i++) {
            li[i] = document.createElement('li');
            if (select_optiones[i].selected == true || select_.value == select_optiones[i].innerHTML ) {
                li[i].className = 'active';
                document.querySelector("[data-indx-select='"+e+"']  > .selecionado_opcion ").innerHTML = select_optiones[i].innerHTML;
            };
            li[i].setAttribute('data-index',i);
            li[i].setAttribute('data-selec-index',e);
// funcion click al selecionar
            li[i].addEventListener( 'click', function(){  _select_option(this.getAttribute('data-index'),this.getAttribute('data-selec-index')); });

            li[i].innerHTML = select_optiones[i].innerHTML;
            ul_cont[0].appendChild(li[i]);

        }; // Fin For select_optiones
    }; // fin for divs_cont_select
} // Fin Function



var cont_slc = 0;
function open_select(idx){
    var idx1 =  idx.getAttribute('data-n-select');
    var ul_cont_li = document.querySelectorAll("[data-indx-select='"+idx1+"'] .cont_select_int > li");
    var hg = 0;
    var slect_open = document.querySelectorAll("[data-indx-select='"+idx1+"']")[0].getAttribute('data-selec-open');
    var slect_element_open = document.querySelectorAll("[data-indx-select='"+idx1+"'] select")[0];
    if (isMobileDevice()) {
        if (window.document.createEvent) { // All
            var evt = window.document.createEvent("MouseEvents");
            evt.initMouseEvent("mousedown", false, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            slect_element_open.dispatchEvent(evt);
        } else if (slect_element_open.fireEvent) { // IE
            slect_element_open.fireEvent("onmousedown");
        }else {
            slect_element_open.click();
        }
    }else {


        for (var i = 0; i < ul_cont_li.length; i++) {
            hg += ul_cont_li[i].offsetHeight;
        };
        if (slect_open == 'false') {
            document.querySelectorAll("[data-indx-select='"+idx1+"']")[0].setAttribute('data-selec-open','true');
            document.querySelectorAll("[data-indx-select='"+idx1+"'] > .cont_list_select_mate > ul")[0].style.height = hg+"px";
            document.querySelectorAll("[data-indx-select='"+idx1+"'] > .icon_select_mate")[0].style.transform = 'rotate(180deg)';
        }else{
            document.querySelectorAll("[data-indx-select='"+idx1+"']")[0].setAttribute('data-selec-open','false');
            document.querySelectorAll("[data-indx-select='"+idx1+"'] > .icon_select_mate")[0].style.transform = 'rotate(0deg)';
            document.querySelectorAll("[data-indx-select='"+idx1+"'] > .cont_list_select_mate > ul")[0].style.height = "0px";
        }
    }

} // fin function open_select

function salir_select(indx){
    var select_ = document.querySelectorAll("[data-indx-select='"+indx+"'] > select")[0];
    document.querySelectorAll("[data-indx-select='"+indx+"'] > .cont_list_select_mate > ul")[0].style.height = "0px";
    document.querySelector("[data-indx-select='"+indx+"'] > .icon_select_mate").style.transform = 'rotate(0deg)';
    document.querySelectorAll("[data-indx-select='"+indx+"']")[0].setAttribute('data-selec-open','false');
}


function _select_option(indx,selc){
    if (isMobileDevice()) {
        selc = selc -1;
    }
    var select_ = document.querySelectorAll("[data-indx-select='"+selc+"'] > select")[0];

    var li_s = document.querySelectorAll("[data-indx-select='"+selc+"'] .cont_select_int > li");
    var p_act = document.querySelectorAll("[data-indx-select='"+selc+"'] > .selecionado_opcion")[0].innerHTML = li_s[indx].innerHTML;
    var select_optiones = document.querySelectorAll("[data-indx-select='"+selc+"'] > select > option");
    for (var i = 0; i < li_s.length; i++) {
        if (li_s[i].className == 'active') {
            li_s[i].className = '';
        };
        li_s[indx].className = 'active';

    };
    select_optiones[indx].selected = true;
    select_.selectedIndex = indx;
    select_.onchange();
    salir_select(selc);
}
