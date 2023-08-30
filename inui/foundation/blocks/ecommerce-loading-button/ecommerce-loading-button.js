$('[data-loading-start]').click(function() {
  $(this).addClass('hide');
  $(this).parent().find('[data-loading-end]').removeClass('hide');
  setTimeout(function() {
    $('[data-loading-start]').removeClass('hide');
    $('[data-loading-end]').addClass('hide');
    $('[data-success-message]').removeClass('hide')
  }, 5000)
});
