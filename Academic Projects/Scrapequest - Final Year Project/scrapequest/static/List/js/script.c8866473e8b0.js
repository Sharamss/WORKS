// When the page loads, display the first project list
document.addEventListener('DOMContentLoaded', () => {
    showProjects('{{ project_counts.keys|first }}');
  });

  function showProjects(org) {
    // Hide all project lists
    const projectLists = document.querySelectorAll('.project-list');
    projectLists.forEach(projectList => {
      projectList.classList.add('hidden');
    });

    // Show the selected project list
    const selectedProjectList = document.getElementById(org);
    selectedProjectList.classList.remove('hidden');
  }