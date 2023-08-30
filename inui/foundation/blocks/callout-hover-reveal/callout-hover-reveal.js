$(function(){
$('[data-callout-hover-reveal]').hover(function(){
  $(this).find('.callout-footer').slideDown(250);
    },function(){
  $(this).find('.callout-footer').slideUp(250);
  });
})
