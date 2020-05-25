number=input('请输入1至100之间的数字：')
while 1:
    temp=int(number)
    if 1<=temp<=100:
        print('You are right！')
        break
    else:
        print('Sorry,try again!')
        number=input('请输入1至100之间的数字：')
