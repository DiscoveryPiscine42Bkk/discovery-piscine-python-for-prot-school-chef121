response = input("What do you have to say?: ")  # รับข้อมูลครั้งแรก
while True:  # เริ่มลูป
    response = input("I got that! Anything else: ")  # ถามคำถามซ้ำ
    if response == "stop":
    
        break  # ออกจากลู