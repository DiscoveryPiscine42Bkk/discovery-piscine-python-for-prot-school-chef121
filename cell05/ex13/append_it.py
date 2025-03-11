import sys

# ตรวจสอบว่ามีพารามิเตอร์ใด ๆ ถูกส่งเข้ามาหรือไม่
if len(sys.argv) == 1:
    print("none")
else:
    for word in sys.argv[1:]:  # วนลูปผ่านพารามิเตอร์ที่ส่งเข้ามา
        if not word.endswith("ism"):  # ถ้าคำลงท้ายด้วย "ism" ให้ข้าม
            print(word + "ism")