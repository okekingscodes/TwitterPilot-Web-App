// get the anchor tags with class "fa-solid"
const faSolidAnchors = document.querySelectorAll('.fa-solid');

// add event listener to the element that triggers the show/hide action
document.getElementById('toggleFaSolid').addEventListener('click', function() {
  // check if the screen is small
  if (window.innerWidth <= 768) { // adjust the value to your desired screen width
    // toggle the display property of the anchor tags
    faSolidAnchors.forEach(anchor => {
      anchor.style.display = anchor.style.display === 'none' ? 'inline-block' : 'none';
    });
  }
});
