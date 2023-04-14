// Get the form and submit button elements
const form = document.querySelector('form');
const submitBtn = document.querySelector('button[type="submit"]');

// Get all the required input elements
const requiredInputs = document.querySelectorAll('input[required]');

// Function to check if all required inputs have a value
function checkRequiredInputs() {
  let allInputsFilled = true;
  requiredInputs.forEach(input => {
    if (!input.value) {
      allInputsFilled = false;
    }
  });
  return allInputsFilled;
}

// Add event listeners to required input elements to check their values
requiredInputs.forEach(input => {
  input.addEventListener('input', () => {
    if (checkRequiredInputs()) {
      submitBtn.disabled = false;
    } else {
      submitBtn.disabled = true;
    }
  });
});

// Disable submit button by default
submitBtn.disabled = true;



// Get the checkbox and login button elements
const checkbox = document.querySelector('input[type="checkbox"]');
const loginBtn = document.querySelector('button[type="submit"]');

// Add event listener to checkbox to enable/disable login button
checkbox.addEventListener('click', () => {
  if (checkbox.checked) {
    loginBtn.disabled = false;
  } else {
    loginBtn.disabled = true;
  }
});

// Disable login button by default
loginBtn.disabled = true;
