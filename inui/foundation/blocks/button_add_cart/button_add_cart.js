$('[data-addCart]').click(function() {
  $(this).addClass('is-adding')
  setTimeout(function() {
  $('[data-addCart]').removeClass('is-adding')
  $('[data-successMessage]').removeClass('hide')
  }, 2500);
});
