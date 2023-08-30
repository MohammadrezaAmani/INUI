$('#primary-menu').on(
  'show.zf.dropdownmenu', function() {
    var dropdown = $(this).find('.is-dropdown-submenu');
    dropdown.css('display', 'none');
    dropdown.fadeIn('slow');
});
$('#primary-menu').on(
  'hide.zf.dropdownmenu', function() {
    var dropdown = $(this).find('.is-dropdown-submenu');
    dropdown.css('display', 'inherit');
    dropdown.fadeOut('slow');
});
