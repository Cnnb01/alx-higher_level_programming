// Write a JavaScript script that fetches from 
// https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of 
// hello from that fetch in the HTML tag DIV#hello.
// The translation of “hello” must be displayed in the HTML tag DIV#hello
$(document).ready(function() {
    $.ajax({
        type:'GET',
        url:'https://hellosalut.stefanbohacek.dev/?lang=fr',
        success: function(response) {
            console.log(response)
            $("div#hello").text(response.hello)
        },
        error: function (error) {
            console.error("Error fetching data", error)
        }
    })
});