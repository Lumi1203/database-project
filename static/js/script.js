document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("darkModeToggle");
    const body = document.body;

    function updateButtonText(isDark) {
        toggleButton.textContent = isDark ? "Light Mode" : "Dark Mode";
    }

    const isDarkMode = localStorage.getItem("theme") === "dark";
    if (isDarkMode) {
        body.classList.add("dark-mode");
    }
    updateButtonText(isDarkMode);

    toggleButton.addEventListener("click", () => {
        const isDark = body.classList.toggle("dark-mode");
        localStorage.setItem("theme", isDark ? "dark" : "light");
        updateButtonText(isDark);
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const passwordInput = document.getElementById("password");
    const confirmPasswordInput = document.getElementById("confirm_password");
    const emailInput = document.getElementById("email");

    form.addEventListener("submit", function (e) {
        const password = passwordInput.value;
        const confirmPassword = confirmPasswordInput.value;
        const email = emailInput.value;

        // Password validation
        const minLength = password.length >= 8;
        const hasUppercase = /[A-Z]/.test(password);
        const hasSpecialChar = /[^A-Za-z0-9]/.test(password);

        if (!minLength || !hasUppercase || !hasSpecialChar) {
            alert("Password must be at least 8 characters long, contain at least one uppercase letter, and one special character.");
            e.preventDefault(); // Prevent form submission
            return;
        }

        // Confirm password match
        if (password !== confirmPassword) {
            alert("Passwords do not match.");
            e.preventDefault();
            return;
        }

        // Email validation
        if (!email.includes("@")) {
            alert("Please enter a valid email address containing '@'.");
            e.preventDefault();
            return;
        }
    });
});

const scrollerDiv = document.getElementById("image-scroller");

if (scrollerDiv) {
    const images = JSON.parse(scrollerDiv.getAttribute("data-images"));
    let currentIndex = 0;
    const scrollerImage = document.getElementById("scroller-image");

    function showNextImage() {
        currentIndex = (currentIndex + 1) % images.length;
        scrollerImage.src = images[currentIndex];
    }

    setInterval(showNextImage, 3000);
}

document.addEventListener('DOMContentLoaded', function () {
    const firstaiderSelect = document.getElementById('firstaider');
    const certificateField = document.getElementById('certificate-field');
    const certInput = document.getElementById('firstaidernumber');

    function toggleCertificateField() {
        if (firstaiderSelect.value === 'Yes') {
            certificateField.style.display = 'block';
            certInput.required = true;
        } else {
            certificateField.style.display = 'none';
            certInput.required = false;
            certInput.value = '';
        }
    }

    toggleCertificateField();

    firstaiderSelect.addEventListener('change', toggleCertificateField);
});
