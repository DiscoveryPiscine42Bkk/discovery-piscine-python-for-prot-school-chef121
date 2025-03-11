a = input("What you gotta say: ") 
print("I got that! Anything else: ", a) 
while True: 
    response = input ("I got that! Anything else ")  
    if response.lower() == "stop":
        break