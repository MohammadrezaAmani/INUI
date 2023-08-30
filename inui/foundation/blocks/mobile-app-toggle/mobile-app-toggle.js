$('[data-mobile-app-toggle] .button').click(function () {
  $(this).siblings().removeClass('is-active');
  $(this).addClass('is-active');
});
