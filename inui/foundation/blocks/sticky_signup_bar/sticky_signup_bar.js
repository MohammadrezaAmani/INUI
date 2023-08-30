(function() {
  var $container = $('#subscription-container');
  var $window = $(window);
  var $footer = $('#email-subscription-footer');
  $(window).on("load scroll", function() {
    var footerOffset = $container.offset().top;
    var myScrollPosition = $window.scrollTop();
    var windowHeight = $window.height();
    var footerHeight = $footer.outerHeight();

    if ((myScrollPosition + windowHeight - footerHeight) > footerOffset) {
      $footer.addClass('is-in-page');
    } else {
      $footer.removeClass('is-in-page');
    }
  });
})();
