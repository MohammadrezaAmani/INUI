var $navList = $('.menu-fancy');

$navList.on('click', 'li:not(.is-selected)', function(e){
  $navList.find(".is-selected").removeClass("is-selected");
  $(e.currentTarget).addClass("is-selected");
});
