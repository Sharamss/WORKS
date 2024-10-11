document.addEventListener('DOMContentLoaded', (event) => {
    let buttons = document.querySelectorAll("[id^='keyword-button-']"); // Select all buttons with IDs starting with 'keyword-button-'
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            showProjects(this.getAttribute('data-target'));
        });
    });
});

function showProjects(baseId) {
    // Hide all project lists
    var projectLists = document.getElementsByClassName('project-list');
    for (var i = 0; i < projectLists.length; i++) {
        projectLists[i].classList.add('hidden');
    }

    // Show the selected full and partial project lists
    var selectedFullProject = document.getElementById(baseId + "-full");
    var selectedPartialProject = document.getElementById(baseId + "-partial");
    
    if (selectedFullProject) {
        selectedFullProject.classList.remove('hidden');
    }
    if (selectedPartialProject) {
        selectedPartialProject.classList.remove('hidden');
    }
}
