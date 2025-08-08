<?php
session_start();
if (!isset($_SESSION['user'])) {
    header("Location: home/index.html");
    exit;
}
?>
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Trang Cá Nhân</title>
</head>
<body>
    <h1>Xin chào, <?php echo htmlspecialchars($_SESSION['user']); ?>!</h1>
    <p>Chào mừng đến trang quản lý in 3D.</p>
    <a href="logout.php">Đăng xuất</a>
</body>
</html>
