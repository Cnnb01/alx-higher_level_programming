// Write a JavaScript script that fetches and lists the title for all movies 
// by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
// All movie titles must be list in the HTML tag UL#list_movies
$(document).ready(function () {
    $.ajax({
        type: 'GET',
        url:  'https://swapi-api.alx-tools.com/api/films/?format=json',
        success: function (response) {
            console.log(response)
            $.each(response.results, function(i, title) {
                $("ul#list_movies").append($("<li></li>").text(title.title));
            });
        },
        error: function (error) {
            console.error("Error fetching data", error)
        }
    });
});