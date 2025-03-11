import sys

# Check if any arguments are provided (except the script name itself)
if len(sys.argv) != 1:
    print("none$")
else:
    # Loop through numbers 0 to 10
    for i in range(13):
        print(f"Table de {i}: ", end="")

        # Inner loop for multiplication results
        for j in range(13):
            print(i * j, end=" ")

        print()  # Newline after each table
