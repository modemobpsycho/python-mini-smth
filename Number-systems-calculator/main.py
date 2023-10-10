main = int(input('Which system do you have? (Answer only with: "2, 8, 10, 16"!) - '))

if main == 10:

    num = int(input('Text your number: '))

    bin_num = bin(num)
    oct_num = oct(num)
    hex_num = hex(num)

    print('binary:', bin_num[2:])
    print('octal:', oct_num[2:])
    print('hexadecimal:', hex_num[2:])

if main != 10:
    num = input('Text your number: ')
    print('decimal:', int(num, main))