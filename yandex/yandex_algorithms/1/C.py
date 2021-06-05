def change_number(tel_number):
    symbols = ['-', '(', ')', '-']
    for item in symbols:
        tel_number = tel_number.replace(item, '')
    tel_number = tel_number.replace('+7', '8')
    if len(tel_number) == 7:
        tel_number = '8495' + tel_number
    return tel_number


tel_number = change_number(input())
for i in range(3):
    if change_number(input()) == tel_number:
        print('YES')
    else:
        print('NO')