function showProjects(id) {
    // Hide all project lists
    var projectLists = document.getElementsByClassName('project-list');
    for (var i = 0; i < projectLists.length; i++) {
        projectLists[i].classList.add('hidden');
    }

    // Show the selected project list
    var selectedProject = document.getElementById(id);
    if (selectedProject) {
        selectedProject.classList.remove('hidden');
    }
}
