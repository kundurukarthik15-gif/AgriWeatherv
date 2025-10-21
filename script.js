const searchBar = document.getElementById("searchBar");
const solutionBox = document.getElementById("solutionBox");

const diseaseSolutions = {
  "blight": "Use copper-based fungicides and rotate crops to prevent blight spread.",
  "rust": "Apply sulfur dusting and resistant crop varieties to control rust.",
  "wilt": "Improve soil drainage, use resistant seeds, and apply bio-fungicides.",
  "mosaic": "Remove infected plants and use virus-free seeds."
};

searchBar.addEventListener("keyup", function(event) {
  let query = event.target.value.toLowerCase().trim();
  if (diseaseSolutions[query]) {
    solutionBox.innerHTML = `<h2>Solution for ${query.charAt(0).toUpperCase() + query.slice(1)}</h2>
                             <p>${diseaseSolutions[query]}</p>`;
  } else if (query === "") {
    solutionBox.innerHTML = `<h2>Solution</h2><p>Search for a disease above to see the solution.</p>`;
  } else {
    solutionBox.innerHTML = `<h2>No Data Found</h2><p>Try another disease name.</p>`;
  }
});
