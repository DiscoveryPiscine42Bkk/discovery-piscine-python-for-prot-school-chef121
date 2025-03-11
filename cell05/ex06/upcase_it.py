import sys

# ตรวจสอบว่ามีอาร์กิวเมนต์เดียวหรือไม่
if len(sys.argv) == 2:
    print(sys.argv[1].upper())  # แปลงข้อความเป็นตัวพิมพ์ใหญ่และแสดงผล
else:
    print("none")