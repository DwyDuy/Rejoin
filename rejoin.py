import subprocess
import time
import random

PLACE_ID = "13379208636"
INTERVAL = 1800 # 30 phút

def get_roblox_packages():
    # Lấy tất cả các package bắt đầu bằng com.roblox.client
    result = subprocess.check_output(["pm", "list", "packages"]).decode("utf-8")
    return [line.replace("package:", "").strip() for line in result.splitlines() if "com.roblox.client" in line]

def loop():
    while True:
        packages = get_roblox_packages()
        print(f"[{time.ctime()}] Tìm thấy {len(packages)} app: {packages}")
        
        for pkg in packages:
            # Kill app
            subprocess.run(["am", "force-stop", pkg])
        
        time.sleep(5) # Nghỉ 5 giây
        
        for pkg in packages:
            # Mở lại bằng Deep Link
            subprocess.run(["am", "start", "-a", "android.intent.action.VIEW", "-d", f"roblox://placeId={PLACE_ID}"])
            time.sleep(random.randint(2, 5)) # Delay né anti-bot
            
        print("Đã hoàn tất vòng lặp, chờ 30 phút...")
        time.sleep(INTERVAL)

if __name__ == "__main__":
    loop()