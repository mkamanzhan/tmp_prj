$(document).ready(function (){
  $("#login-plus").on( "mouseover", function() {
      $('#user-menu').css('visibility','visible')
  })
  $('#main').on( "mouseover", function() {
    $('#user-menu').css('visibility','hidden')
  })

    })

$(window).scroll(function() {
    var target = $(this).scrollTop();
    if(target < 200) {
       $('#slip-menu').css('visibility', 'hidden');
       $('#slip-menu').css('position', 'absolut');
       $('#slip-menu').css('top', '-100px');
       $('#slip-menu').css('transition', 'all .2s');
       $('#user-menu').css('top', '150px');
    }
    else {
       $('#slip-menu').css('visibility', 'visible');
       $('#slip-menu').css('position', 'sticky');
       $('#slip-menu').css('top', '-1px');
       $('#slip-menu').css('transition', 'all .5s');
       $('#user-menu').css('top', '150px');
    }
 })

