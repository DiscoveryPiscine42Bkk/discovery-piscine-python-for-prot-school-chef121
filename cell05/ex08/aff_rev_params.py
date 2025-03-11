import sys

# ตรวจสอบว่ามีอาร์กิวเมนต์มากกว่า 1 หรือไม่
if len(sys.argv) < 3:
    print("none")
else:
    for arg in reversed(sys.argv[1:]):  # เรียงลำดับย้อนกลับและแสดงผล
        print(arg)