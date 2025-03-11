import sys
import re

# ตรวจสอบว่ามีอาร์กิวเมนต์ครบ 2 ตัวหรือไม่
if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    text = sys.argv[2]
    
    # ใช้ re.findall() เพื่อนับจำนวนครั้งที่ keyword ปรากฏใน text
    matches = re.findall(rf'\b{re.escape(keyword)}\b', text)

    if matches:
        print(len(matches))
    else:
        print("none")