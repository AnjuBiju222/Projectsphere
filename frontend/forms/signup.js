const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});

// form data
function submitSignupForm(event) {
    event.preventDefault(); // Prevent the default form submission

    // Get form data
    const form = document.getElementById('signup-form');
    const username = form.querySelector('input[type="text"]').value;
    const email = form.querySelector('input[type="email"]').value;
    const password = form.querySelector('input[type="password"]').value;

    // You can do further validation here if needed

    // Display the captured data (for testing purposes)
    console.log("Username:", username);
    console.log("Email:", email);
    console.log("Password:", password);

    // Now you can send this data to your backend or perform other actions as needed
}

// login.js

// Get the login link element
const loginLink = document.getElementById('login-link');

// Add an event listener to the login link
loginLink.addEventListener('click', (event) => {
    event.preventDefault(); // Prevent default link behavior

    // Get the selected radio button value
    const userType = document.querySelector('input[name="userType"]:checked').value;

    // Redirect based on the selected radio button value
    switch (userType) {
        case 'student':
            window.location.href = '../home.html'; // Redirect to studenthome.html for student
            break;
        case 'staff':
            window.location.href = '../guide/guide.html'; // Redirect to staffhome.html for staff
            break;
        case 'coordinator':
            window.location.href = '../coordinator/coordinator-home.html'; // Redirect to coordinatorhome.html for coordinator
            break;
        default:
            // Handle default case or error
            console.error('Invalid user type selected');
    }
});

// Function to submit the signup form
function submitSignupForm(event) {
    // Add form submission logic here (if needed)
}
