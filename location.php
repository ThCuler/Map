<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

// مسیر پوشه ذخیره سازی
$dir = "location";

// اگر پوشه وجود نداشت، بسازش
if (!is_dir($dir)) {
    mkdir($dir, 0777, true);
}

// دریافت داده‌ها از فرم POST
$data = $_POST;

// فایل دیباگ برای مشاهده داده‌های دریافتی (هر بار بازنویسی می‌شود)
file_put_contents("debug.txt", "POST DATA:\n" . print_r($data, true));

// بررسی داده‌ها و ذخیره در فایل جدید
if (!empty($data) && isset($data['lat']) && isset($data['lon'])) {
    $filename = $dir . "/location_" . date("Ymd_His") . "_" . uniqid() . ".json";
    file_put_contents($filename, json_encode($data, JSON_PRETTY_PRINT));
    echo "Saved to: $filename";
} else {
    echo "No valid data received.";
}
?>
