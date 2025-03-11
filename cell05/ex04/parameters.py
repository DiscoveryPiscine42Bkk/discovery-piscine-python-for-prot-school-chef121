import sys

# นับจำนวนพารามิเตอร์ที่ส่งเข้ามา (ไม่นับชื่อไฟล์)
num_params = len(sys.argv) - 1

# แสดงผลจำนวนพารามิเตอร์
print(f"Number of parameters: {num_params}")