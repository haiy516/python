##闰年判定
while 1:
    temp=input('请输入一个年份(输入end结束程序):')
    year=int(temp)
    if temp=='end':
        exit()
    elif year%400==0:
        print(temp,'是闰年！')
    elif (year%4==0)and(year%100!=0):
        print(temp,'是闰年！')
    else:
        print(temp,'不是闰年！')