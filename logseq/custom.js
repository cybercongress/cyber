// change theme to black
if (document.querySelector("html").getAttribute("data-theme") === "light") {
  document.querySelector("html").setAttribute("data-theme", "dark");

  document.querySelector("body").classList.remove("light-theme");
  document.querySelector("body").classList.remove("white-theme");
  document.querySelector("body").classList.add("dark-theme");
}

document.querySelector(".journals-nav .flex-1").innerHTML = "Blog";
