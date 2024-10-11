// Function to show the projects associated with the clicked button
function showProjects(id) {
    // Select all project list containers
    const projectLists = document.querySelectorAll('.project-list');
  
    // Loop through all project list containers
    projectLists.forEach((projectList) => {
      // Check if the projectList id matches the button id clicked
      if(projectList.id === id) {
        // If it matches, remove the 'hidden' class to show the list
        projectList.classList.remove('hidden');
      } else {
        // If it doesn't match, add the 'hidden' class to hide the list
        projectList.classList.add('hidden');
      }
    });
  }
  
  // Event listener for when the DOM is fully loaded
  document.addEventListener('DOMContentLoaded', () => {
    // Select the first project button within the buttons container
    const firstProjectButton = document.querySelector('.flex.flex-wrap button');
  
    // If the first project button exists, simulate a click on it
    if(firstProjectButton) {
      firstProjectButton.click();
    }
  });
  