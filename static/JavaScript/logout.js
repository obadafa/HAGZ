const logout_btn = document.querySelector(".logout");

logout_btn.addEventListener("click", (e) => {
  localStorage.setItem("login", "false");
});
