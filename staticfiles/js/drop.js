// In your JavaScript file
document.addEventListener("DOMContentLoaded", function () {
    const dropdownButton = document.getElementById("profile-dropdown");
    const dropdownMenu = document.getElementById("profile-dropdown-menu");

    dropdownButton.addEventListener("click", function () {
        dropdownMenu.classList.toggle("hidden");
    });

    // Close dropdown if clicked outside
    window.addEventListener("click", function (event) {
        if (!dropdownButton.contains(event.target)) {
            dropdownMenu.classList.add("hidden");
        }
    });
});
