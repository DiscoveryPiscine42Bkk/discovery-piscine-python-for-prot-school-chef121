import sys

# ตรวจสอบว่ามีอาร์กิวเมนต์เดียวหรือไม่
if len(sys.argv) == 2:
    print(sys.argv[1].lower())  # แปลงข้อความเป็นตัวพิมพ์เล็กและแสดงผล
else:
    print("none") 