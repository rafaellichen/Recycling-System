$(function() {
    $('#recycleType').autocomplete({
      source: "/api/types/"
      //$('.ui-autocomplete').css({ 'left': x + 'px', 'top': y + 'px'});
    })
});