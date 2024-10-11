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
