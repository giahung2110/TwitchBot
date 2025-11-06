# ============================================================
# main2.py — SwitchAuto Client (Tool khách)
# ✅ Kết nối API bot Telegram để kiểm tra key
# ✅ Lưu cache key theo IP/ngày
# ✅ Auto click “GET” mỗi 60 giây
# ✅ Hiện IP, số vòng, tổng follow
# ============================================================

import sys
import time
import requests
import threading
import json
import os
import shutil
from datetime import datetime, date
from colorama import Fore, init
init(autoreset=True)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# ================== CONFIG ==================
API_BASE = "https://daphine-nonsocialistic-kimbery.ngrok-free.dev"
TARGET_URL = "https://q9tx.stackauth.online/follow.html"
CACHE_FILE = os.path.join(os.path.dirname(__file__), "used_key_cache.json")
GET_COOLDOWN = 60
FOLLOW_PER_GET = 100
USE_DRIVER_MANAGER = True

# ================== UI ==================
def banner():
    b = f"""
    \033[97m   ██╗  ██╗ ██████╗ ███████╗ █████╗ ███╗   ██╗███████╗██╗   ██╗    \033[95m
    \033[97m   ██║  ██║██╔════╝ ██╔════╝██╔══██╗████╗  ██║╚══███╔╝██║   ██║    \033[95m
    \033[97m   ███████║██║  ███╗███████╗███████║██╔██╗ ██║  ███╔╝ ██║   ██║     \033[95m
    \033[97m   ██╔══██║██║   ██║╚════██║██╔══██║██║╚██╗██║ ███╔╝  ██║   ██║      \033[95m
    \033[97m   ██║  ██║╚██████╔╝███████║██║  ██║██║ ╚████║███████╗╚██████╔╝     \033[95m
    \033[97m   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝ ╚═════╝     \033[95m

    \033[96m   TooL Tích Hợp  - TĂNG TƯƠNG TÁC TỰ ĐỘNG       \033[95m
    \033[97m   Phiên bản: 2.0.0 | Phát triển: Gia Hưng - TooL    \033[95m
    \033[93m       ⏰ Ngày: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
    """
    print(b)

def print_status(ip, run_count, total_follow, remaining):
    now = datetime.now().strftime("%H:%M:%S")
    sys.stdout.write(
        Fore.CYAN
        + f"\r[{now}] 🌍 IP: {ip} | Lần: {run_count} | Tổng: +{total_follow} | Đang chờ {remaining:02d}s ..."
    )
    sys.stdout.flush()

# ================== HELPERS ==================
def get_public_ip():
    try:
        r = requests.get("https://api.ipify.org", timeout=3)
        if r.status_code == 200:
            return r.text.strip()
    except:
        pass
    return "unknown"

def load_cache():
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_cache(data):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def key_cached_for_today(ip, cache):
    today = date.today().isoformat()
    if ip in cache and cache[ip]["date"] == today:
        return cache[ip]["key"]
    return None

def store_key_cache(ip, key):
    cache = load_cache()
    cache[ip] = {"key": key, "date": date.today().isoformat()}
    save_cache(cache)

def check_key_valid_api(key):
    try:
        r = requests.get(f"{API_BASE}/api/check_key?key={key}", timeout=10)
        if r.status_code != 200:
            return False, "Lỗi kết nối API"
        data = r.json()
        if data.get("valid"):
            return True, data.get("expiry_date", "unknown")
        else:
            return False, data.get("reason", "Key không hợp lệ")
    except Exception as e:
        return False, f"Lỗi API: {e}"

def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")

    if USE_DRIVER_MANAGER:
        svc = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=svc, options=options)
    else:
        driver = webdriver.Chrome(options=options)
    return driver

# ================== MAIN LOGIC ==================
def auto_loop(username, stop_event):
    ip = get_public_ip()
    run_count = 0
    total_follow = 0

    try:
        driver = create_driver()
        driver.get(TARGET_URL)
        print(Fore.GREEN + f"🌐 Đã mở trang: {TARGET_URL}")
    except WebDriverException as e:
        print(Fore.RED + f"❌ Lỗi khởi tạo trình duyệt: {e}")
        return

    while not stop_event.is_set():
        clicked = False
        try:
            elems = driver.find_elements(By.XPATH, "//button[contains(translate(text(),'GET','get'),'get')]")
            if elems:
                for el in elems:
                    try:
                        if el.is_displayed() and el.is_enabled():
                            el.click()
                            clicked = True
                            break
                    except:
                        continue
            else:
                driver.refresh()
        except Exception as e:
            print(Fore.YELLOW + f"⚠️ Lỗi khi click GET: {e}")

        if clicked:
            run_count += 1
            total_follow += FOLLOW_PER_GET
            print(Fore.GREEN + f"\n✅ +{FOLLOW_PER_GET} Follow (vòng {run_count})")
        else:
            print(Fore.YELLOW + "\n⚠️ Không tìm thấy nút GET, thử lại sau 60s")

        for remaining in range(GET_COOLDOWN, 0, -1):
            if stop_event.is_set():
                break
            print_status(ip, run_count, total_follow, remaining)
            time.sleep(1)
        print()

# ================== MAIN ==================
def main():
    banner()
    ip = get_public_ip()
    cache = load_cache()
    cached_key = key_cached_for_today(ip, cache)

    if cached_key:
        ok, msg = check_key_valid_api(cached_key)
        if ok:
            print(Fore.GREEN + f"🔁 Đã dùng key hôm nay — Hết hạn: {msg}")
            key = cached_key
        else:
            print(Fore.YELLOW + f"⚠️ Key cache không hợp lệ: {msg}")
            key = input(Fore.CYAN + "🔑 Nhập key VIP mới: ").strip()
            ok, msg = check_key_valid_api(key)
            if not ok:
                print(Fore.RED + f"❌ {msg}")
                sys.exit(1)
            store_key_cache(ip, key)
    else:
        key = input(Fore.CYAN + "🔑 Nhập key VIP của bạn: ").strip()
        ok, msg = check_key_valid_api(key)
        if not ok:
            print(Fore.RED + f"❌ {msg}")
            sys.exit(1)
        print(Fore.GREEN + f"✅ Key hợp lệ — Hết hạn: {msg}")
        store_key_cache(ip, key)

    username = input(Fore.CYAN + "👤 Nhập username Twitch: ").strip()
    if not username:
        print(Fore.RED + "🚫 Bạn chưa nhập username.")
        sys.exit(1)

    stop_event = threading.Event()
    t = threading.Thread(target=auto_loop, args=(username, stop_event), daemon=True)
    t.start()

    print(Fore.GREEN + "\n🔁 Tool đang chạy vô hạn. Nhấn Ctrl+C để dừng.")
    try:
        while t.is_alive():
            t.join(timeout=1)
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n✋ Dừng tool...")
        stop_event.set()
        t.join(timeout=5)

if __name__ == "__main__":
    main()
