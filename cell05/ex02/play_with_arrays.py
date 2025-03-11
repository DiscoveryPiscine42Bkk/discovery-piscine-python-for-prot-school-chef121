original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# กรองเฉพาะค่าที่มากกว่า 5 และสร้างอาร์เรย์ใหม่โดยบวก 2 กับค่าเหล่านั้น
new_array = [x + 2 for x in original_array if x > 5]

# แสดงผลลัพธ์
print(original_array)
print(new_array)