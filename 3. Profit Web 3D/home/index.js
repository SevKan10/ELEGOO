document.getElementById("calcForm").addEventListener("submit", async function (e) {
  e.preventDefault();
  const form = e.target;
  const formData = new FormData(form);
  const jsonData = {};

  formData.forEach((value, key) => {
    jsonData[key] = value;
  });

  const response = await fetch("/api/tinh", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(jsonData),
  });

  const result = await response.json();
  const output = document.getElementById("ketQua");

  if (result.error) {
    output.innerText = "Lỗi: " + result.error;
  } else {
    output.innerText = `
Thời gian in: ${result.thoi_gian_str}
Tiền nhựa: ${result.tien_nhua.toLocaleString()} VNĐ
Tiền điện: ${result.tien_dien.toLocaleString()} VNĐ
Hao mòn máy: ${result.tien_hao_mon.toLocaleString()} VNĐ
Tiền công: ${result.tien_cong.toLocaleString()} VNĐ
----------------------------
Tổng chi phí: ${result.tong_chi_phi.toLocaleString()} VNĐ
Giá bán (có lời): ${result.gia_ban.toLocaleString()} VNĐ
Tổng lời: ${result.loi_nhuan_vnd.toLocaleString()} VNĐ
    `;
  }
});

