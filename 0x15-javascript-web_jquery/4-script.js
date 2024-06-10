// when the user clicks on the tag DIV#red_header
// document.querySelector('header').style.color = '#FF0000';
// $('header').css('color', '#FF0000')
// $('#red_header').on("click",function() {
//     $('header').addClass('red');
// });
$(document).ready(function() {
    $("#toggle_header").on("click", function() {
        if ($("header").hasClass("red")) {
            $("header").removeClass("red").addClass("green");
        }else{
            $("header").removeClass("green").addClass("red");
        }
    })
});