import sys

def shrink(s):
    # Shrink the string to the first 8 characters
    print(s[:8])

def enlarge(s):
    # Enlarge the string to exactly 8 characters by appending 'Z'
    print(s.ljust(8, 'Z'))

def main():
    # If no arguments are provided, print 'none'
    if len(sys.argv) < 2:
        print("none$")
    else:
        # Iterate over each argument passed to the program
        for arg in sys.argv[1:]:
            if len(arg) > 8:
                shrink(arg)
            elif len(arg) < 8:
                enlarge(arg)
            else:
                print(arg)

if __name__ == "__main__":
    main()