$('[data-mobile-app-filter-menu] li').click(function () {
  $(this).siblings().removeClass('is-active');
  $(this).addClass('is-active');
});
