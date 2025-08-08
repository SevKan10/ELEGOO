<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $email = $_POST['email'] ?? '';
    $password = $_POST['password'] ?? '';

    $file = fopen("accounts.txt", "r");
    $found = false;

    while (($line = fgets($file)) !== false) {
        list($stored_email, $stored_hash) = explode("|", trim($line));
        if ($stored_email === $email && password_verify($password, $stored_hash)) {
            $found = true;
            $_SESSION['user'] = $email;
            break;
        }
    }
    fclose($file);

    if ($found) {
        echo "Đăng nhập thành công";
    } else {
        http_response_code(401);
        echo "Sai email hoặc mật khẩu";
    }
} else {
    http_response_code(405);
    echo "Phương thức không hợp lệ";
}
?>
