 
$('.search-button').click(function(){
  $(this).parent().toggleClass('open');
});

$('.search-box').on('keydown', e => {
  console.log('keydown', e.which);
  if(e.which == 13) {
    $.post("", {
      topic : e.target.value
    });
  }
});
