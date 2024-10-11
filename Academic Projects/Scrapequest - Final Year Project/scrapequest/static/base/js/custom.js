// Search button
function toggleSearchResults(expand) {
    if (expand) {
        $("#search-results").addClass('expanded').fadeIn('slow');
    } else {
        $("#search-results").removeClass('expanded').fadeOut('slow');
    }
}

function fetchSearchResults() {
    var query = $("#search-input").val();
    var searchUrl = $("#search-container").data('search-url');

    if (query.length > 0) {
        if (!$("#search-results").hasClass('expanded')) {
            toggleSearchResults(true);
        }
        $.ajax({
            url: searchUrl,
            data: { 'search': query },
            success: function(data) {
                $("#search-results").html(data.html);
            }
        });
    } else {
        toggleSearchResults(false);
    }
}

// Close the search results if the user clicks outside
$(document).click(function(event) {
    if (!$(event.target).closest('#search-container').length) {
        toggleSearchResults(false);
    }
});

function performSearch(keyword) {
    $("#search-input").val(keyword);
    fetchSearchResults();
}


//Predefined Keywords button
function toggleKeywords() {
    var dropdownContent = document.getElementById("keyword-dropdown");
    if (dropdownContent.style.display === "none") {
        dropdownContent.style.display = "block";
    } else {
        dropdownContent.style.display = "none";
    }
}

function fetchProjectsByKeyword(keyword) {
    $.ajax({
        url: '/projects/',  // Endpoint defined in urls.py
        type: 'GET',
        data: {'keyword': keyword},
        success: function(response) {
            $('#main-content').html(response);
        },
        error: function(error) {
            console.error("Error fetching projects: ", error);
        }
    });
}

// Attach toggle function to button
document.getElementById("predefined-keywords-btn").onclick = toggleKeywords;