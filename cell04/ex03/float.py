num = input("Give me a number: ")

# แปลงค่าที่ป้อนเป็น float
try:
    num = float(num)
    # ตรวจสอบว่าค่าที่ป้อนเป็นจำนวนเต็มหรือไม่
    if num.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    print("Invalid input. Please enter a valid number.")