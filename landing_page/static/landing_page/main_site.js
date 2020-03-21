// General variables
var $mainMenuItem = $(".mainMenuItem");

// Unlimited main menu events after mouseover
$mainMenuItem.on('mouseenter', function () {
    $(this).animate({
        width: 265,
        height: 265,
    }, 250);
    $(this).find('img').addClass("mainMenuShadow");
    var $descriptionDiv = $("<div class='mainMenuDesc'>DIVDIVDIV</div>");
//   Description div addition
//    $(this).before($descriptionDiv);
});

// Unlimited main menu events after mouseleave
$mainMenuItem.on("mouseleave", function () {
    $(this).animate({
        width: 250,
        height: 250,
    }, 250);
    $(this).find('img').removeClass("mainMenuShadow");
//    Description div removal
//    $(this).siblings('.mainMenuDesc').remove();
});