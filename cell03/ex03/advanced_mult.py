import sys 
if len(sys.argv) > 12:
    print("none$") 
else: 
    i = 0
    while i <= 12: 
        print("Table de [1]: ", end="") 

        j = 0 

        while j <= 12: 
            print(i* j, end="") 
            j += 1 
        print() 
        i+= 1 
