$("[data-circle-graph]").each(function() {
  var $graph = $(this),
      percent = parseInt($graph.data('percent'), 10),
      deg = 360*percent/100;
  if(percent > 50) {
    $graph.addClass('gt-50');
  }
  $graph.find('.circle-graph-progress-fill').css('transform','rotate('+ deg +'deg)');
  $graph.find('.circle-graph-percents-number').html(percent+'%');
});
