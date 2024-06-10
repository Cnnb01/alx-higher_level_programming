// Write a JavaScript script that adds the class red to the <header> element
// when the user clicks on the tag DIV#red_header
// document.querySelector('header').style.color = '#FF0000';
// $('header').css('color', '#FF0000')
$('#red_header').on("click",function() {
    $('header').addClass('red');
});