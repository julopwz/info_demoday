// MENU NAVBAR -----------------------------------
var offset = $('#meuMenu').offset().top;
var $meuMenu = $('#meuMenu');
$(document).on('scroll', function () {
    if (offset <= $(window).scrollTop()) {
        $meuMenu.addClass('fixar');
    } else {
        $meuMenu.removeClass('fixar');
    }
});

// SLIDE ---------------------------------
window.addEventListener('scroll', function(e){
  var scrolled = window.pageYOffset;
  var parallax = document.querySelector(".parallax");
  // You can adjust the 0.4 to change the speed
	var coords = (scrolled * 0.4) + 'px'
  parallax.style.transform = 'translateY(' + coords + ')';
});