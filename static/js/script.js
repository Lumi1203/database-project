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
