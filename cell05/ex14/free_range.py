import sys

# ตรวจสอบว่ามีพารามิเตอร์ถูกส่งเข้ามาและมีจำนวน 2 ค่า
if len(sys.argv) != 3:
    print("none")
else:
    try:
        start = int(sys.argv[1])  # แปลงพารามิเตอร์แรกเป็นจำนวนเต็ม
        end = int(sys.argv[2])    # แปลงพารามิเตอร์ที่สองเป็นจำนวนเต็ม
        print(list(range(start, end + 1)))  # ใช้ range() และแปลงเป็น list ก่อนพิมพ์ออกมา
    except ValueError:
        print("none")