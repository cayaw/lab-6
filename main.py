
# lab by caya wilcox
def encode(encoded):
    s = ""
    for c in encoded:
        s += str((int(c)+3) % 10)
    return s


def decode(encoded_p): #hey its lorenzo i just reversed your function that you made basically

    s=""
    for c in encoded_p:
        s+= str((int(c)-3)%10)
    return s

def main(): #Change i made was to made it loop inside the main until quit was selected in the menu

    loop_continue= True
    while loop_continue:
        print("Menu")
        print("-------------")
        print("1. Encode\n2. Decode\n3. Quit")
        choice = input("Please enter an option: ")
        if choice == "1":
            p_to_encode = input("Please enter your password to encode: ")
            encoded_p = encode(p_to_encode)
            print("Your password has been encoded and stored!")
        if choice == "2":
            print(f"The encoded password is {encoded_p}, and the original password is {decode(encoded_p)}")
        if choice == "3":
            loop_continue=False
            quit()


if __name__ == "__main__":
    main()