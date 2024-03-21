def menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')


def encode(password):
    encoded_password = ''
    for char in password:
        if char.isalpha():
            shifted = ord(char) - 1
        if char.isnumeric():
            shifted = ord(char) + 2
        encoded_password += chr(shifted)
    return encoded_password


def decode(encoded_password):
    pass


if __name__ == '__main__':
    menu_option = 0
    password = ''
    encoded_password = ''
    prog_run = True
    while prog_run == True:
        menu()
        menu_option = input('Please enter an option: ')
        if menu_option == '1':
            password = input('Please enter your password to encode: ')
            encoded_password = encode(password)
            print(f'Your password has been encoded and stored!:')
            print(encoded_password)
        elif menu_option == '2':
            password = decode(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {password}.')
        elif menu_option == '3':
            prog_run = False

