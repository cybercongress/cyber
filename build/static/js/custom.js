document.documentElement.setAttribute("data-theme", "dark");
document.documentElement.setAttribute("data-color", "green");

document.documentElement.classList.add("dark");

document.body.classList.add("dark-theme");
document.body.classList.remove("light-theme");
document.body.classList.remove("white-theme");

document.querySelector(".journals-nav .flex-1").innerHTML = "Blog";
