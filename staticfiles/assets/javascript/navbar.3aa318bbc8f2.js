$(window).scroll(function(){
    if ($(window).scrollTop()) {
  $('.navbar').addClass('bg-dark testex');
  $('.navbar').removeClass('bg-primary teste');
    } else {
  $('.navbar').removeClass('bg-dark testex');
  $('.navbar').addClass('bg-primary teste');
    }
    if ($(window).scrollTop() > 100) {
  $('.navbar').removeClass('teste');
  } else {
  $('.navbar').addClass('teste');
    }
});