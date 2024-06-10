// Write a JavaScript script that fetches the character name from this URL:
// https://swapi-api.alx-tools.com/api/people/5/?format=json
// The name must be displayed in the HTML tag DIV#character

$(document).ready(function () {
    $.ajax({
        type: 'GET',
        url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
        success: function (response) {
            console.log(response)
            $("div#character").text(response.name)
        },
        error: function (error) {
            console.error("Error fetching data", error)
        }
    })
});