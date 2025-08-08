const loginForm = document.getElementById("login-form");
const registerForm = document.getElementById("register-form");

document.getElementById("go-register").onclick = () => {
  loginForm.style.display = "none";
  registerForm.style.display = "block";
};

document.getElementById("back-login").onclick = () => {
  loginForm.style.display = "block";
  registerForm.style.display = "none";
};

document.getElementById("forgot-password").onclick = () => {
  alert("Tính năng này sẽ có sau.");
};

// Đăng nhập
loginForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  const formData = new FormData();
  formData.append("email", email);
  formData.append("password", password);

  const res = await fetch("process_login.php", {
    method: "POST",
    body: formData,
  });

  const text = await res.text();
  if (res.ok) {
    alert(text);
    window.location.href = "index.html";
  } else {
    alert("Lỗi: " + text);
  }
});

// Đăng ký
registerForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const email = document.getElementById("reg-email").value;
  const password = document.getElementById("reg-password").value;
  const confirm = document.getElementById("reg-confirm").value;

  if (password !== confirm) {
    alert("Mật khẩu không khớp");
    return;
  }

  const formData = new FormData();
  formData.append("email", email);
  formData.append("password", password);

  const res = await fetch("process_register.php", {
    method: "POST",
    body: formData,
  });

  const text = await res.text();
  if (res.ok) {
    alert(text);
    loginForm.style.display = "block";
    registerForm.style.display = "none";
  } else {
    alert("Lỗi: " + text);
  }
});
