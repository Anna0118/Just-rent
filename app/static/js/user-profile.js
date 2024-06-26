document.addEventListener("DOMContentLoaded", function () {
  fetch("/api/profile")
    .then((response) => response.json())
    .then((data) => {
        // 兩個template不能一樣，否則只會讀取第一個就填入了
      document.getElementById("img_username").textContent = data.username;
      document.getElementById("img_email").textContent = data.email;
      document.getElementById("username").value = data.username;
      document.getElementById("email").value = data.email,
      document.getElementById("phone_number").value = data.phone_number
    })
    .catch((error) => console.error("Error fetching profile:", error));
});
