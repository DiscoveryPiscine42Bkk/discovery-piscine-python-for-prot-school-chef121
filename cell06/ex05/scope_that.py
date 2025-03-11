def add_one(x):
    # Adds 1 to the parameter passed
    return x + 1

def main():
    # Initialize the variable
    number = 5
    
    # Display the initial value of the variable
    print(f"Initial value: {number}")
    
    # Call the method that adds 1 to the variable
    number = add_one(number)
    
    # Display the value of the variable again after calling the method
    print(f"Value after adding 1: {number}")

if __name__ == "__main__":
    main()