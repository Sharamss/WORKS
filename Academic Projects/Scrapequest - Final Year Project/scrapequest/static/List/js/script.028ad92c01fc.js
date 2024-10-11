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

function saveProject(button) {
    // Simulate a save action
    button.classList.add('opacity-0');
    setTimeout(() => {
      button.classList.add('hidden');
      let successMessage = button.nextElementSibling;
      successMessage.classList.remove('hidden');
      successMessage.classList.add('opacity-100');
    }, 600);
  
    // Reset the state after some time
    setTimeout(() => {
      let successMessage = button.nextElementSibling;
      successMessage.classList.add('opacity-0');
      successMessage.classList.add('hidden');
      button.classList.remove('hidden');
      button.classList.remove('opacity-0');
    }, 3600);
  }