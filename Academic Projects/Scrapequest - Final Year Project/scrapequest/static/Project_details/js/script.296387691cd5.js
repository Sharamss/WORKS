function showProjects(id) {
    // Select all project list containers
    const projectLists = document.querySelectorAll('.project-list');

    // Loop through all project list containers to hide them
    projectLists.forEach((projectList) => {
        projectList.classList.add('hidden'); // Use Tailwind's 'hidden' class to hide
    });

    // Find and display the selected project list
    const selectedProject = document.getElementById(id);
    if (selectedProject) {
        selectedProject.classList.remove('hidden'); // Use Tailwind's 'hidden' class to show
    }
}

// Event listener for when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // Select the first project button within the buttons container
    const firstProjectButton = document.querySelector('.flex.flex-wrap button');

    // If the first project button exists, simulate a click on it to show its associated projects
    if (firstProjectButton) {
        firstProjectButton.click();
    }
});
