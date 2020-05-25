#三次机会输入密码
i=1
password='fish'
print('请您输入密码：')
while 1:
    temp=input()
    if password==temp:
        print('密码正确，正在登录......')
        break
    elif '*' in temp:
        if i==4:
            print('输入密码次数已用完。')
            break
        else:
            print('密码中不能有"*”，您还有',4-i,'次输入机会，请重新输入：')
    else:
        if i == 3:
            print('输入密码次数已用完。')
            break
        else:
            print('密码错误，您还有', 3 - i, '次输入机会，请重新输入：')
        i+=1