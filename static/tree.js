// Runs in the browser after the HTML is on the page.
document.querySelectorAll(".tree-toggle").forEach((button) => {
  button.addEventListener("click", () => {
    const childList = button.nextElementSibling;
    childList.classList.toggle("is-open");
    button.classList.toggle("is-open")
  });
});
