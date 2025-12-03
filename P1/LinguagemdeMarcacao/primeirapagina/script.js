document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.createElement("button");
    toggleButton.innerText = "Alternar Modo Escuro";
    toggleButton.classList.add("dark-mode-toggle");

    document.body.prepend(toggleButton);

    if (localStorage.getItem("dark-mode") === "enabled") {
        document.body.classList.add("dark-mode");
    }

    toggleButton.addEventListener("click", function () {
        document.body.classList.toggle("dark-mode");

        // Salva a preferência no localStorage
        if (document.body.classList.contains("dark-mode")) {
            localStorage.setItem("dark-mode", "enabled");
        } else {
            localStorage.setItem("dark-mode", "disabled");
        }
    });
});
