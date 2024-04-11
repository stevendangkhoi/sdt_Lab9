
def encode(num):
    return num+3

def decode(num):
    return num-3

def main():
    storeNum = None
    encodedNum = ''
    decodedNum = ''
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        choice = int(input("Please enter an option: "))
        if choice == 1:
            pw = input("Please enter your password to encode: ")
            for n in pw:
                encodedNum += str(encode(int(n)))
                storeNum = encodedNum
            print("Your password has been encoded and stored!\n")
        elif choice == 2:
            for n in storeNum:
                decodedNum += str(decode(int(n)))
            print("The encoded password is " + encodedNum + ", and the original password is " + decodedNum + ".\n")
        elif choice == 3:
            break


if __name__ == "__main__":
    main()
