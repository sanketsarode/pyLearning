import re
decrypted = b"abcdefghijklmnopqrstuvwxyzABCDEFGHIJK12345@#$67890LMNOPQRSTUVWXYZ "
encrypted = b"qwertyuiopasdfgh1234567890jklzxcvbnmQA@#$ZXSWEDCVFRTGBNHYUJMKIOLP "

encrypt_table = bytes.maketrans(decrypted, encrypted)
decrypt_table = bytes.maketrans(encrypted, decrypted)

result = ''
choice = ''
message = ''

while choice != '0':
    choice = input("Options:\n1. Encrypt\n2. Decrypt\n0. Exit Program: ")

    if choice == '1':
        message = input('\nEnter the ReferenceID: ')
        if len(message) == 12 and re.search('[a-z]', message) and re.search('[A-Z]', message) and re.search('[0-9]', message) and not re.search('[@#$]', message):
            result = message.translate(encrypt_table)
            print(result)
        else:
            print("\nShould have length as 12 and not special characters")

    elif choice == '2':
        message = input('\nEnter Decrypted ReferenceID: ')
        result = message.translate(decrypt_table)
        print(result)

    elif choice != '0':
        print('You have entered an invalid input, please try again. \n\n')