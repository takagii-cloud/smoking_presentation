document.addEventListener("DOMContentLoaded", function() {
    var btn = document.getElementById("menubtn");
    var menu = document.getElementById("menu");

    btn.addEventListener("click", function() {
        menu.classList.toggle("hidden");
    });
});
