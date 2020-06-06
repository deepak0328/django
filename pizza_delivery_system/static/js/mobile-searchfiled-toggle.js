$(document).ready(function() {
    $('.show-search').click(function() {
      $(this).next().delay(5000).toggleClass('toggle');
    });
  });