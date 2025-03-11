import sys

# ตรวจสอบว่ามีพารามิเตอร์ส่งเข้ามาหรือไม่
if len(sys.argv) > 1:
    print(sys.argv[1])  # แสดงพารามิเตอร์ตัวแรก
else:
    print("none")
    