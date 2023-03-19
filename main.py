
# lab by caya wilcox
def encode(encoded):
    s = ""
    for c in encoded:
        s += str((int(c)+3) % 10)
    return s


def decode(encoded_p):
    pass


if __name__ == "__main__":
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
        quit()