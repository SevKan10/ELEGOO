<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $email = $_POST['email'] ?? '';
    $password = $_POST['password'] ?? '';

    if (!$email || !$password) {
        http_response_code(400);
        echo "Thiếu thông tin";
        exit;
    }

    $hashed = password_hash($password, PASSWORD_DEFAULT);

    $file = fopen("accounts.txt", "a+");
    while (($line = fgets($file)) !== false) {
        list($stored_email) = explode("|", trim($line));
        if ($stored_email === $email) {
            fclose($file);
            http_response_code(409);
            echo "Email đã tồn tại";
            exit;
        }
    }
    fwrite($file, "$email|$hashed\n");
    fclose($file);
    echo "Đăng ký thành công";
} else {
    http_response_code(405);
    echo "Phương thức không hợp lệ";
}
?>
