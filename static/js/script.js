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
