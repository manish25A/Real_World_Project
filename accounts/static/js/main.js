AOS.init({
    duration: 800,
    easing: 'slide',
    once: false
});

jQuery(document).ready(function ($) {

    "use strict";


    var siteMenuClone = function () {

        $('.js-clone-nav').each(function () {
            var $this = $(this);
            $this.clone().attr('class', 'site-nav-wrap').appendTo('.site-mobile-menu-body');
        });


        setTimeout(function () {

            var counter = 0;
            $('.site-mobile-menu .has-children').each(function () {
                var $this = $(this);

                $this.prepend('<span class="arrow-collapse collapsed">');

                $this.find('.arrow-collapse').attr({
                    'data-toggle': 'collapse',
                    'data-target': '#collapseItem' + counter,
                });

                $this.find('> ul').attr({
                    'class': 'collapse',
                    'id': 'collapseItem' + counter,
                });

                counter++;

            });

        }, 1000);

        $('body').on('click', '.arrow-collapse', function (e) {
            var $this = $(this);
            if ($this.closest('li').find('.collapse').hasClass('show')) {
                $this.removeClass('active');
            } else {
                $this.addClass('active');
            }
            e.preventDefault();

        });

        $(window).resize(function () {
            var $this = $(this),
                w = $this.width();

            if (w > 768) {
                if ($('body').hasClass('offcanvas-menu')) {
                    $('body').removeClass('offcanvas-menu');
                }
            }
        })

        $('body').on('click', '.js-menu-toggle', function (e) {
            var $this = $(this);
            e.preventDefault();

            if ($('body').hasClass('offcanvas-menu')) {
                $('body').removeClass('offcanvas-menu');
                $this.removeClass('active');
            } else {
                $('body').addClass('offcanvas-menu');
                $this.addClass('active');
            }
        })

        // click outisde offcanvas
        $(document).mouseup(function (e) {
            var container = $(".site-mobile-menu");
            if (!container.is(e.target) && container.has(e.target).length === 0) {
                if ($('body').hasClass('offcanvas-menu')) {
                    $('body').removeClass('offcanvas-menu');
                }
            }
        });
    };
    siteMenuClone();


    var sitePlusMinus = function () {
        $('.js-btn-minus').on('click', function (e) {
            e.preventDefault();
            if ($(this).closest('.input-group').find('.form-control').val() != 0) {
                $(this).closest('.input-group').find('.form-control').val(parseInt($(this).closest('.input-group').find('.form-control').val()) - 1);
            } else {
                $(this).closest('.input-group').find('.form-control').val(parseInt(0));
            }
        });
        $('.js-btn-plus').on('click', function (e) {
            e.preventDefault();
            $(this).closest('.input-group').find('.form-control').val(parseInt($(this).closest('.input-group').find('.form-control').val()) + 1);
        });
    };
    // sitePlusMinus();


    var siteSliderRange = function () {
        $("#slider-range").slider({
            range: true,
            min: 0,
            max: 500,
            values: [75, 300],
            slide: function (event, ui) {
                $("#amount").val("$" + ui.values[0] + " - $" + ui.values[1]);
            }
        });
        $("#amount").val("$" + $("#slider-range").slider("values", 0) +
            " - $" + $("#slider-range").slider("values", 1));
    };
    // siteSliderRange();


    var siteMagnificPopup = function () {
        $('.image-popup').magnificPopup({
            type: 'image',
            closeOnContentClick: true,
            closeBtnInside: false,
            fixedContentPos: true,
            mainClass: 'mfp-no-margins mfp-with-zoom', // class to remove default margin from left and right side
            gallery: {
                enabled: true,
                navigateByImgClick: true,
                preload: [0, 1] // Will preload 0 - before current, and 1 after the current image
            },
            image: {
                verticalFit: true
            },
            zoom: {
                enabled: true,
                duration: 300 // don't foget to change the duration also in CSS
            }
        });

        $('.popup-youtube, .popup-vimeo, .popup-gmaps').magnificPopup({
            disableOn: 700,
            type: 'iframe',
            mainClass: 'mfp-fade',
            removalDelay: 160,
            preloader: false,

            fixedContentPos: false
        });
    };
    siteMagnificPopup();


    var siteCarousel = function () {
        if ($('.nonloop-block-13').length > 0) {
            $('.nonloop-block-13').owlCarousel({
                center: false,
                items: 1,
                loop: true,
                stagePadding: 0,
                autoplay: true,
                margin: 20,
                nav: true,
                dots: true,
                navText: ['<span class="icon-arrow_back">', '<span class="icon-arrow_forward">'],
                responsive: {
                    600: {
                        margin: 20,
                        stagePadding: 0,
                        items: 1
                    },
                    1000: {
                        margin: 20,
                        stagePadding: 0,
                        items: 2
                    },
                    1200: {
                        margin: 20,
                        stagePadding: 0,
                        items: 3
                    }
                }
            });
        }


        if ($('.nonloop-block-14').length > 0) {
            $('.nonloop-block-14').owlCarousel({
                center: false,
                items: 1,
                loop: true,
                stagePadding: 0,
                autoplay: true,
                margin: 20,
                nav: true,
                dots: true,
                navText: ['<span class="icon-arrow_back">', '<span class="icon-arrow_forward">'],
                responsive: {
                    600: {
                        margin: 20,
                        stagePadding: 0,
                        items: 1
                    },
                    1000: {
                        margin: 20,
                        stagePadding: 0,
                        items: 2
                    }

                }
            });
        }

        if ($('.nonloop-block-15').length > 0) {
            var owl2 = $('.nonloop-block-15');
            owl2.owlCarousel({
                center: false,
                items: 1,
                loop: true,
                stagePadding: 0,
                autoplay: true,
                margin: 20,
                nav: true,
                dots: true,
                navText: ['<span class="icon-arrow_back">', '<span class="icon-arrow_forward">'],
                responsive: {
                    600: {
                        margin: 20,
                        stagePadding: 0,
                        items: 1,
                        nav: false,
                        dots: true
                    },
                    1000: {
                        margin: 20,
                        stagePadding: 0,
                        items: 2,
                        nav: true,
                        dots: true
                    },
                    1200: {
                        margin: 20,
                        stagePadding: 0,
                        items: 3,
                        nav: true,
                        dots: true
                    }
                }
            });
            $('.owl-custom-next').click(function (e) {
                e.preventDefault();
                owl.trigger('next.owl.carousel');
            });
            $('.owl-custom-prev').click(function (e) {
                e.preventDefault();
                owl.trigger('prev.owl.carousel');
            });
        }


        if ($('.nonloop-block-16').length > 0) {
            var owl = $('.nonloop-block-16');
            owl.owlCarousel({
                center: false,
                items: 1,
                loop: true,
                stagePadding: 0,
                autoplay: true,
                margin: 20,
                nav: false,
                dots: true,
                autoHeight: true,
                navText: ['<span class="icon-arrow_back">', '<span class="icon-arrow_forward">'],
                responsive: {
                    600: {
                        margin: 20,
                        stagePadding: 0,
                        items: 1,
                        nav: false,
                        dots: true
                    },
                    1000: {
                        margin: 20,
                        stagePadding: 0,
                        items: 1,
                        nav: false,
                        dots: true
                    },
                    1200: {
                        margin: 20,
                        stagePadding: 0,
                        items: 1,
                        nav: false,
                        dots: true
                    }
                }
            });

            $('.owl-custom-next').click(function (e) {
                e.preventDefault();
                owl.trigger('next.owl.carousel');
            });
            $('.owl-custom-prev').click(function (e) {
                e.preventDefault();
                owl.trigger('prev.owl.carousel');
            });
        }


        if ($('.slide-one-item').length > 0) {
            $('.slide-one-item').owlCarousel({
                center: false,
                items: 1,
                loop: true,
                stagePadding: 0,
                margin: 0,
                autoplay: true,
                pauseOnHover: false,
                animateOut: 'fadeOut',
                animateIn: 'fadeIn',
                nav: true,
                navText: ['<span class="icon-arrow_back">', '<span class="icon-arrow_forward">']
            });
        }
    };
    siteCarousel();

    var siteStellar = function () {
        $(window).stellar({
            responsive: false,
            parallaxBackgrounds: true,
            parallaxElements: true,
            horizontalScrolling: false,
            hideDistantElements: false,
            scrollProperty: 'scroll'
        });
    };
    siteStellar();

    var siteCountDown = function () {

        if ($('#date-countdown').length > 0) {
            $('#date-countdown').countdown('2020/10/10', function (event) {
                var $this = $(this).html(event.strftime(''
                    + '<span class="countdown-block"><span class="label">%w</span> weeks </span>'
                    + '<span class="countdown-block"><span class="label">%d</span> days </span>'
                    + '<span class="countdown-block"><span class="label">%H</span> hr </span>'
                    + '<span class="countdown-block"><span class="label">%M</span> min </span>'
                    + '<span class="countdown-block"><span class="label">%S</span> sec</span>'));
            });
        }

    };
    siteCountDown();

    var siteDatePicker = function () {

        if ($('.datepicker').length > 0) {
            $('.datepicker').datepicker();
        }

    };
    siteDatePicker();


    var windowScrolled = function () {


        $(window).scroll(function () {

            var $w = $(this), st = $w.scrollTop(), navbar = $('.js-site-navbar');

            if (st > 100) {
                navbar.addClass('scrolled');
            } else {
                navbar.removeClass('scrolled');
            }

        })

    }
    windowScrolled();

});


console.clear();
(function () {
    "use strict";

    var bulletClasses = {
        elements: {
            container: ".pindicator",
            bullet: ".bullet",
        },
        helpers: {
            past: "past",
            current: "current",
            next: "next",
            future: "future",
        }
    };

    var bulletEls;
    document.addEventListener("DOMContentLoaded", initBullets);

    function initBullets() {
        bulletEls = Array.prototype.slice.call(
            document.body.querySelectorAll(bulletClasses.elements.bullet)
        );
        bulletEls.forEach(function (el) {
            el.addEventListener("mousedown", function (event) {
                gotoPage(bulletEls.indexOf(this) + 1);
            });
            el.addEventListener("touchstart", function (event) {
                event.preventDefault();
                gotoPage(bulletEls.indexOf(this) + 1);
            });
        });
    }

    function gotoPage(pageNum) {
        bulletEls.forEach(function (e) {
            e.classList.remove.apply(e.classList,
                Object.keys(bulletClasses.helpers).map(function (e) {
                    return bulletClasses.helpers[e];
                })
            )
        });
        bulletEls[pageNum - 1].classList.add(bulletClasses.helpers.current);
        if (pageNum > 1) {
            for (var i = 0; i < pageNum; i++) {
                bulletEls[i].classList.add(bulletClasses.helpers.past);
            }
        }
        if (pageNum < bulletEls.length) {
            bulletEls[pageNum].classList.add(bulletClasses.helpers.next);
            for (var i = bulletEls.length - 1; i >= pageNum; i--) {
                bulletEls[i].classList.add(bulletClasses.helpers.future);
            }
        }
    }
})();


var placeSearch, autocomplete;
var componentForm = {
    street_number: 'short_name',
    route: 'long_name',
    locality: 'long_name',
    administrative_area_level_1: 'short_name',
    country: 'long_name',
    postal_code: 'short_name'
};

function initAutocomplete() {
    // Create the autocomplete object, restricting the search to geographical
    // location types.
    autocomplete = new google.maps.places.Autocomplete(
        /** @type {!HTMLInputElement} */(document.getElementById('autocomplete')),
        {types: ['geocode']});

    // When the user selects an address from the dropdown, populate the address
    // fields in the form.
    autocomplete.addListener('place_changed', fillInAddress);
}

function fillInAddress() {
    // Get the place details from the autocomplete object.
    var place = autocomplete.getPlace();

    for (var component in componentForm) {
        document.getElementById(component).value = '';
        document.getElementById(component).disabled = false;
    }

    // Get each component of the address from the place details
    // and fill the corresponding field on the form.
    for (var i = 0; i < place.address_components.length; i++) {
        var addressType = place.address_components[i].types[0];
        if (componentForm[addressType]) {
            var val = place.address_components[i][componentForm[addressType]];
            document.getElementById(addressType).value = val;
        }
    }
}

// Bias the autocomplete object to the user's geographical location,
// as supplied by the browser's 'navigator.geolocation' object.
function geolocate() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {
            var geolocation = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };
            var circle = new google.maps.Circle({
                center: geolocation,
                radius: position.coords.accuracy
            });
            autocomplete.setBounds(circle.getBounds());
        });
    }
}


/*search*/
const charactersList = document.getElementById('charactersList');
const searchBar = document.getElementById('searchBar');
let hpCharacters = [];

searchBar.addEventListener('keyup', (e) => {
    const searchString = e.target.value.toLowerCase();

    const filteredCharacters = hpCharacters.filter((character) => {
        return (
            character.name.toLowerCase().includes(searchString) ||
            character.house.toLowerCase().includes(searchString)
        );
    });
    displayCharacters(filteredCharacters);
});

const loadCharacters = async () => {
    try {
        const res = await fetch('professionals.html');
        hpCharacters = await res.json();
        displayCharacters(hpCharacters);
    } catch (err) {
        console.error(err);
    }
};

const displayCharacters = (characters) => {
    const htmlString = characters
        .map((character) => {
            return `
            <li class="character">
                <h2>${character.name}</h2>
                <p>House: ${character.house}</p>
                <img src="${character.image}"></img>
            </li>
        `;
        })
        .join('');
    charactersList.innerHTML = htmlString;
};

loadCharacters();



