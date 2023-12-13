// Function to toggle between login and register forms
function toggleForm(formId) {
    const loginContainer = document.getElementById("loginContainer");
    const registerContainer = document.getElementById("registerContainer");

    if (formId === "registerContainer") {
        loginContainer.style.display = "none";
        registerContainer.style.display = "block";
    } else {
        loginContainer.style.display = "block";
        registerContainer.style.display = "none";
    }
}

// Function to handle user sign-in
function signIn() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const role = document.getElementById("role").value;

    // Use Firebase authentication
    signInWithEmailAndPassword(auth, username, password)
        .then((userCredential) => {
            // Signed in
            const user = userCredential.user;
            console.log(user);
            // Display success message
            displayMessage("success", "Successfully signed in!");
            // Redirect to index.html
            window.location.href = "index.html";
        })
        .catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;
            console.error(errorMessage);
            // Display error message
            displayMessage("error", errorMessage);
        });
}

// Function to handle user registration
function register() {
    const newUsername = document.getElementById("new-username").value;
    const newPassword = document.getElementById("new-password").value;
    const newRole = document.getElementById("new-role").value;

    // Use Firebase authentication
    createUserWithEmailAndPassword(auth, newUsername, newPassword)
        .then((userCredential) => {
            // Registered and signed in
            const user = userCredential.user;
            console.log(user);
            // Display success message
            displayMessage("success", "Successfully registered and signed in!");
            // Redirect to index.html
            window.location.href = "index.html";
        })
        .catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;
            console.error(errorMessage);
            // Display error message
            displayMessage("error", errorMessage);
        });
}

// Function to display messages
function displayMessage(type, message) {
    const messageContainer = document.createElement("div");
    messageContainer.className = `message ${type}`;
    messageContainer.textContent = message;

    // Append the message container to the body
    document.body.appendChild(messageContainer);

    // Remove the message after a few seconds (adjust as needed)
    setTimeout(() => {
        document.body.removeChild(messageContainer);
    }, 3000);
}
