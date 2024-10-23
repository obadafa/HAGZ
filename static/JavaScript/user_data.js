const name_title = document.querySelector(".name_title");

const id = localStorage.getItem("id");
const user_name = localStorage.getItem("name");
const email = localStorage.getItem("email");
const user_status = localStorage.getItem("status");
const login = localStorage.getItem("login");

name_title.innerHTML = `Welcome, ${
  user_name.charAt(0).toUpperCase() + user_name.slice(1)
}!`;

