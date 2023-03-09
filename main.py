"""
Author: John Crawford
Lab 6: Software Engineering
"""


def print_menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print('')


def encode(password):
    encoded_password = ''
    for digit in password:
        if int(digit) >= 7:
            encoded_password += str(int(digit) + 3)[-1]
        else:
            encoded_password += str(int(digit) + 3)
    return encoded_password


def decode(encoded_password):
    decoded_password = ""
    for ch in encoded_password:
        if int(ch) >= 3:
            decoded_password += str(int(ch) - 3)
        else:
            decoded_password += str(10 - (3 - int(ch)))
    return decoded_password


def main():
    while True:
        print_menu()
        user_input = input('Please enter an option: ')

        if user_input == '1':
            password = input('Please enter your password to encode: ')
            encoded_password = encode(password)
            print(encoded_password)
            print('Your password has been encoded and stored! \n')

        elif user_input == '2':
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.\n")

        elif user_input == '3':
            break


if __name__ == '__main__':
    main()