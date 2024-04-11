def encode(num):
    return num+3

def decode(num):
    return num-3

def main():
    storeNum = None
    encodedNum = ''
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        choice = int(input("Please enter an option: "))
        if choice == 1:
            pw = input("Please enter your password to encode: ")
            storeNum = int(pw)
            for n in pw:
                encodedNum += str(encode(int(n)))
            print("Your password has been encoded and stored!\n")
        elif choice == 2:
            print("The encoded password is " + encodedNum + ", and the original password is " + pw + ".\n")
        elif choice == 3:
            break


if __name__ == "__main__":
    main()
