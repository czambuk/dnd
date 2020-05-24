// General variables
var $mainMenuItem = $(".mainMenuItem");

// Unlimited main menu events after mouseover
$mainMenuItem.on('mouseenter', function () {
    $(this).animate({
        "width" : "105%",
        "height" : "105%",
    }, 100);
    $(this).find('img').addClass("mainMenuShadow");
    $(this).children('div .mainMenuDesc').removeClass('hidden');
});

// Unlimited main menu events after mouseleave
$mainMenuItem.on("mouseleave", function () {
    $(this).animate({
        "width" : "100%",
        "height" : "100%",
    }, 100);
    $(this).find('img').removeClass("mainMenuShadow");
    $(this).children('div .mainMenuDesc').addClass('hidden');
});

