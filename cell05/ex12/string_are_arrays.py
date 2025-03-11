import sys

# ตรวจสอบว่ามีพารามิเตอร์เดียวหรือไม่
if len(sys.argv) != 2:
    print("none")
else:
    text = sys.argv[1]
    result = "z" * text.count("z")  # สร้างสตริงที่มีจำนวน 'z' เท่ากับที่พบในข้อความ
    print(result if result else "none")