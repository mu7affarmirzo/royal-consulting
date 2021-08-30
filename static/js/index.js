$(document).ready(function () {
    $("#map path").click(function (e) {
        $("#map-title").html($(this).attr("data-title"));
        $("#area-data").html($(this).attr("data-area"));
        $("#population-data").html($(this).attr("data-population"));
        $("#overall-gdp").html($(this).attr("data-gdp"));
        $("#percapita-gdp").html($(this).attr("data-percapita-gdp"));

        e.stopPropagation();
        $("#map path:not(.text)").css("fill", "#C8C832");
        $(this).css("fill", "#0066CC");
    });
    $(document).click(function (e) {
        $("#map path:not(.text)").css("fill", "#C8C832");

        $("#map-title").html($("#map-title").attr("data-default"));
        $("#area-data").html($("#area-data").attr("data-default"));
        $("#population-data").html($("#population-data").attr("data-default"));
        $("#overall-gdp").html($("#overall-gdp").attr("data-default"));
        $("#percapita-gdp").html($("#percapita-gdp").attr("data-default"));
    });

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
            if (scrollTop - prev.top > -700 && $(window).width() > 576) {
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
            } else if ($(window).width() < 576 && scrollTop - prev.top > -750) {
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
            } else {
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
});

$(document).ready(function () {
    $(document).keydown(function (e) {
        var selText = "";
        if (document.getSelection) {
            selText = document.getSelection().toString();
        } else if (document.selection) {
            selText = document.selection.createRange().text;
        } else if (window.getSelection) {
            selText = window.getSelection().toString();
        }
        if (selText != "") {
            var alertTexts = {
                errorDetected:
                    "There is a mistake in the text: '" +
                    selText.toString() +
                    "'\n\n",
                enterCorrectText: "Enter the correct option",
                thanks: "Thank you! Your message has been sent to admission.",
                similarText:
                    "The erroneous text and the proposed option may not be the same",
                emptyText: "No text entered",
                tooLongText:
                    "To send an error message select a block of text with an error sized from 3 to 20 characters",
                connectionError:
                    "An error occurred. Please, check your internet connection",
            };
            e = e || window.event;
            if (e.ctrlKey && e.keyCode == 13) {
                var curUrl = window.location.href;
                var lang = curUrl.split("/")[3];
                console.log(lang);
                var protocol = window.location.protocol;
                var hostname = window.location.hostname;
                if (selText.length > 2 && selText.length < 20) {
                    s = prompt(
                        alertTexts.errorDetected,
                        alertTexts.enterCorrectText
                    );
                    if (s != "" && s != null) {
                        if (selText != s) {
                            // $.ajax({
                            //     url:
                            //         protocol +
                            //         "//" +
                            //         hostname +
                            //         "/uz/site/check-text",
                            //     type: "post",
                            //     data: {
                            //         errText: selText,
                            //         correctText: s,
                            //         curl: curUrl,
                            //     },
                            //     success: function (response) {
                            //         if (response == "SUCCESS") {
                            //             alert(alertTexts.thanks);
                            //         } else {
                            //             alert(alertTexts.connectionError);
                            //         }
                            //     },
                            //     error: function () {
                            //         alert(
                            //             alertTexts.connectionError + "..."
                            //         );
                            //     },
                            // });
                        } else {
                            alert(alertTexts.similarText + "...");
                        }
                    } else {
                        alert(alertTexts.emptyText + "...");
                    }
                } else {
                    alert(alertTexts.tooLongText + "...");
                }
            }
        }
    });
});
