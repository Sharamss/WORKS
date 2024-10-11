function showProjects(id) {
    // Hide all project lists by removing the 'active' class
    var projectLists = document.getElementsByClassName("project-list");
    for (var i = 0; i < projectLists.length; i++) {
        projectLists[i].classList.remove("active");
    }

    // Show the selected project list by adding the 'active' class
    var selectedProject = document.getElementById(id);
    selectedProject.classList.add("active");
}
