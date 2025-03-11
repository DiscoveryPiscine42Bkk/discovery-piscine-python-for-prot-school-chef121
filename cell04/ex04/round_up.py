import math

# รับค่าจากผู้ใช้
num = input("Give me a number: ")

try:
    # แปลงค่าเป็น float
    num = float(num)

    # ปัดขึ้นเป็นจำนวนเต็ม
    rounded_num = math.ceil(num)

    # แสดงผล
    print(rounded_num)

except ValueError:
    print("Invalid input. Please enter a valid number.")