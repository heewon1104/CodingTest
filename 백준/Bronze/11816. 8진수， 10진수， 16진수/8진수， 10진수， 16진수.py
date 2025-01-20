str = input()

if(str[0] == '0'):
    if(str[1] == 'x'):
        print(int(str, 16))
    else:
        print(int(str, 8))
else:
    print(int(str))