def encode(num):
    pass

def decode(num):
    pass

def main():
    storeNum = None
    while True:
        print("Menu\n-------------\n1. Encode2. \nDecode3. Quit\n")
        choice = int(input("Please enter an option: "))
        if choice == 1:
            pw = input("Please enter your password to encode: ")
            storeNum = int(pw)
            
        elif choice == 2:
            pass
        elif choice == 3:
            False


if __name__ == "__main__":
    main()
