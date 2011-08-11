(function($){
  var small = $('.small_left').find('div');

  small.hover(function(e){
    var sibling = $(this).parent().siblings('a');
    sibling.css({
      background: ' #682121',
      color: 'white'
    });
  }, function(e){
    var sibling = $(this).parent().siblings('a');
    sibling.css({
      background: '',
      color: ''
    });
  });

})(jQuery);
