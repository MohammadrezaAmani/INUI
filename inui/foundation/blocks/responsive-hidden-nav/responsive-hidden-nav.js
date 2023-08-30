var $topBar = $('[data-responsive-hidden-nav]');
var $button = $('[data-responsive-hidden-nav] .responsive-hidden-button');
var $visibleLinks = $('[data-responsive-hidden-nav] .visible-links');
var $hiddenLinks = $('[data-responsive-hidden-nav] .hidden-links');

var responsiveBreaks = []; // Empty List (Array) on initialization

function updateTopBar() {
  
  var availableSpace = $button.hasClass('hidden') ? $topBar.width() : $topBar.width() - $button.width() - 30; // Calculation of available space on the logic of whether button has the class `hidden` or not

  if($visibleLinks.width() > availableSpace) { // Logic when visible list is overflowing the nav
    
    responsiveBreaks.push($visibleLinks.width()); // Record the width of the list
    $visibleLinks.children().last().prependTo($hiddenLinks); // Move item to the hidden list
    
    // Show the resonsive hidden button
    if($button.hasClass('hidden')) {
      $button.removeClass('hidden');
    }
  
  } else { // Logic when visible list is not overflowing the nav
    
    if(availableSpace > responsiveBreaks[responsiveBreaks.length-1]) { // Logic when there is space for another item in the nav
      $hiddenLinks.children().first().appendTo($visibleLinks);
      responsiveBreaks.pop(); // Move the item to the visible list
    }
    
    // Hide the resonsive hidden button if list is empty
    if(responsiveBreaks.length < 1) {
      $button.addClass('hidden');
      $hiddenLinks.addClass('hidden');
    }
  }

  $button.attr("count", responsiveBreaks.length); // Keeping counter updated

  if($visibleLinks.width() > availableSpace) { // Occur again if the visible list is still overflowing the nav
    updateTopBar();
  }
}

// Window listeners
$(window).resize(function() {
    updateTopBar();
});
$button.on('click', function() {
  $hiddenLinks.toggleClass('hidden');
});
updateTopBar();
