# 🚀 Hướng dẫn chạy `TwitchAuto`

Tập tin này chứa hướng dẫn chi tiết để chạy tool **Selenium TwitchAuto** mà bạn đã được cung cấp.  
Công cụ này giúp tự động buff Follow Twitch cho bạn.  
> ⚠️ **Lưu ý:** Chỉ sử dụng tool cho các trang bạn tạo hoặc được phép test, **không dùng cho mục đích spam hoặc gây hại**.

---

## 🧰 Yêu cầu

- 🐍 Python **3.12+**
- 🌐 Kết nối Internet để tải **ChromeDriver** tự động  
- 💻 Cài đặt sẵn **Google Chrome (hoặc Chromium)**
- 📦 Thư viện Python:
  - `selenium`
  - `webdriver-manager`
  - *(khuyến nghị thêm)* `colorama` để hiển thị màu sắc sinh động trong terminal

---

## ⚙️ Cài đặt

1️⃣ **(Khuyến nghị)**: Tạo môi trường ảo `venv` để cách ly dependencies:

```bash
python -m venv venv
# Mac/Linux
source venv/bin/activate
# Windows (PowerShell)
venv\Scripts\Activate.ps1
```

2️⃣ **Cài đặt các thư viện cần thiết:**

---

## ⚙️ CÀI ĐẶT NHANH 🔧

### 🪟 Windows
Chạy file sau trong thư mục tool:
```bash
install_requirements.bat
```
File này sẽ tự động cài đặt các thư viện cần thiết.

### 🐧 Linux / macOS
Mở terminal và chạy:
```bash
chmod +x install_requirements.sh
./install_requirements.sh
```

---

## ▶️ Cách chạy cơ bản

```bash
python main.py --username "giahung2110" --delay 60
```

📘 **Giải thích tham số:**
| Tham số | Ý nghĩa |
|----------|----------|
| `--url` | 🌐 api của admin đã sẵn sàng buff *(bắt buộc)* |
| `--username` | 👤 Username Twitch cần điền *(bắt buộc)* |
| `--delay` | ⏳ Thời gian chờ giữa mỗi vòng lặp *(mặc định: 60 giây)* |

---

## 🧠 Tuỳ chọn nâng cao

- 🕶️ `--headless` → Chạy trình duyệt ở **chế độ ẩn** (không mở cửa sổ Chrome)
- 🔁 `--max-iterations N` → Dừng sau **N lần chạy** *(0 = chạy vô hạn)*
- 📸 `--screenshot-on-error` → Lưu ảnh khi gặp lỗi
- ⏱️ `--timeout SECS` → Giới hạn thời gian load trang *(mặc định 15s)*

💡 **Ví dụ:**
```bash
python main.py --username "giahung2110" --delay 60 --headless --max-iterations 10 --screenshot-on-error
```

---

## 💻 Chạy trên Windows (gợi ý)

1. 🪟 Mở **PowerShell**
2. 🔹 Kích hoạt môi trường `venv`
3. 🚀 Chạy lệnh:
   ```bash
   python main.py --username "..." --delay 60
   ```
4. 🧩 Nếu gặp lỗi:
   - Cập nhật lại `webdriver-manager`
   - Đảm bảo Chrome được cài và **cùng kiến trúc (64-bit)** với hệ điều hành

---

## 🛠️ Troubleshooting (Xử lý lỗi)

| 🧩 Vấn đề | 🔍 Cách xử lý |
|-----------|---------------|
| ❌ Không tìm thấy ô nhập | Gửi HTML hoặc screenshot phần input để chỉnh selector |
| ⚠️ Không nhấn được nút GET | Trang có thể có lớp bảo vệ – thử thêm độ trễ `time.sleep(2)` |
| ⌛ Timeout khi load | Tăng `--timeout` lên 20–30 |
| 🧱 Lỗi ChromeDriver | Kiểm tra phiên bản Chrome hoặc cập nhật `webdriver-manager` |

---

## 📄 Ghi log & Nâng cao

- 📝 Có thể thêm chức năng **ghi log ra file** (ví dụ `main.log`) để lưu lại mọi hoạt động.  
- ⚙️ Có thể biến tool thành **Windows Service** hoặc **Linux Daemon** để chạy nền 24/7.
- 🧱 Mình có thể hỗ trợ thêm `systemd unit` (Linux) hoặc `Task Scheduler` (Windows) nếu bạn cần.

---

## 🔄 Hai chế độ sử dụng

| Chế độ | Mô tả |
|--------|-------|
| 🕶️ **Ẩn Chrome (headless)** | Dùng `main.py — chạy ngầm, tiết kiệm tài nguyên |

---

## 💬 Gợi ý thêm

- 📁 Có thể tạo file `run.bat` (Windows) hoặc `run.sh` (Linux) để chạy nhanh chỉ 1 lệnh  
- 🧠 Nếu bạn gửi mình **HTML phần input/button**, mình có thể chỉnh lại selector chính xác hơn  
- 🎨 Bạn có thể thêm **màu, emoji, log file** để terminal của bạn đẹp và chuyên nghiệp hơn!  

---

## 🏁 Kết luận

✨ Tool ` main2.py` là bản Selenium tự động hóa tiện dụng, có thể:
- Tự động điền username 🎯  
- Tự động click nút GET +100 FOLLOWERS 💥  
- Tự động chờ delay và lặp lại 🔁  
- Chạy ẩn hoặc hiển tuỳ ý 🌗  

---

💡 **Nếu bạn muốn mình tạo thêm:**
- 🧾 File log `.log` chuyên nghiệp  
- 🪄 Giao diện CLI có thanh tiến trình  
- 🧰 File `.bat` chạy nhanh trên Windows  

→ Hãy bảo mình biết, mình sẽ tạo luôn cho bạn ⚡
---

## 📞 Thông Tin Liên Hệ

> Liên hệ qua các mạng xã hội sau:

- 🌐 [Facebook](https://www.facebook.com/congtuannhon2110/)
- 💬 [Zalo](https://zalo.me/0989870742)
- ✈️ [Telegram](https://t.me/hungsanzu2110)

---

### ©️ Copyright 2025 — **GiaHung**
> Mọi quyền được sao lưu.  
> Nếu bạn sử dụng lại mã nguồn, vui lòng ghi rõ nguồn: [GiaHungzZ].
