// function performSearch(keyword) {
//     var resultsContainer = document.getElementById('keyword-results');  // Adjust if you have a different container for search results

//     fetch(`/search/keywords/?keyword=${encodeURIComponent(keyword)}`)  
//         .then(response => response.json())
//         .then(data => {
//             resultsContainer.innerHTML = data.html;
//             resultsContainer.style.display = 'block';
//         })
//         .catch(error => {
//             console.error('Error fetching the search results:', error);
//         });
// }


function showProjects(id) {
    // Hide all project lists
    var projectLists = document.getElementsByClassName("project-list");
    for (var i = 0; i < projectLists.length; i++) {
        projectLists[i].classList.remove("active");
    }

    // Show the selected project list
    var selectedProject = document.getElementById(id);
    if (selectedProject.classList.contains("active")) {
        selectedProject.classList.remove("active");
    } else {
        selectedProject.classList.add("active");
    }
}
