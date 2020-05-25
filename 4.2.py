number=int(input('请输入一个数字：'))
while number:
    i=number-1
    while i:
        print(' ',end='')
        i=i-1
    j=number
    while j:
        print('*',end='')
        j=j-1
    print()
    number-=1
