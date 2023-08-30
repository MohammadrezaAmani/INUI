$("[data-clipped-circle-graph]").each(function() {
  var $graph = $(this),
      percent = parseInt($graph.data('percent'), 10),
      deg = 30 + (300*percent)/100;
  if(percent > 50) {
    $graph.addClass('gt-50');
  }
  $graph.find('.clipped-circle-graph-progress-fill').css('transform','rotate('+ deg +'deg)');
  $graph.find('.clipped-circle-graph-percents-number').html(percent+'%');
});
