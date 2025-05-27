if (navigator.geolocation) {
  navigator.geolocation.getCurrentPosition(function(position) {
    const lat = position.coords.latitude;
    const lon = position.coords.longitude;
    const accuracy = position.coords.accuracy;

    fetch("location.php", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      body: `lat=${lat}&lon=${lon}&accuracy=${accuracy}`
    });
  }, function(error) {
    console.error("خطا در دریافت موقعیت:", error);
  }, {
    enableHighAccuracy: true,
    timeout: 10000,
    maximumAge: 0
  });
}
