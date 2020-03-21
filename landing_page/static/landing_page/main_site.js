var $mainMenuItem = $(".mainMenuItem");

$mainMenuItem.on('mouseenter', function () {
    $(this).animate({
        width: 265,
        height: 265,
    }, 250);
    $(this).find('img').addClass("mainMenuShadow");
});
$mainMenuItem.on("mouseleave", function () {
    $(this).animate({
        width: 250,
        height: 250,
    }, 250);
    $(this).find('img').removeClass("mainMenuShadow");
});