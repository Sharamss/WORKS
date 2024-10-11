  // When the page loads, display the first project list
  document.addEventListener('DOMContentLoaded', () => {
    // Automatically click the first project button to show its projects
    const firstProjectButton = document.querySelector('#keyword-buttons-container button');
    if (firstProjectButton) {
      firstProjectButton.click();
    }
  });

  function showProjects(id) {
    // Hide all project lists
    const projectLists = document.querySelectorAll('.project-list');
    projectLists.forEach(projectList => {
      projectList.classList.add('hidden');
    });

    // Show the selected project list
    const selectedProjectList = document.getElementById(id);
    if (selectedProjectList) {
      selectedProjectList.classList.remove('hidden');
    }
}
