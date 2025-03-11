def greetings(name="noble stranger"):
    if isinstance(name, str):
        print(f"Hello, {name}.")
    else:
        print("Error! It was not a name.")

# ทดสอบฟังก์ชัน
greetings("Chayanun")
greetings("Chalongnantachai")
greetings()
greetings(17)