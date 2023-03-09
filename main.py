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
            encoded_password += str(int(digit) += 3)[-1]
        else:
            encoded_password += str(int(digit) += 3)
    return encoded_password

def main():
    while True:
        print_menu()
        user_input = input('Please enter an option: ')

        if user_input == '1':
            password = input('Please enter your password to encode: ')
            print(encode(password))
            print('Your password has been encoded and stored! \n')

        elif user_input == '2':
            pass

        elif user_input == '3':
            break
if __name__ == '__main__':
    main()