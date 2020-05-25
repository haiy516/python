#作者：王辉
#日期：2020/3/10
#时间：22:43
def gcd(x,y):
    if x<y:
        x,y=y,x
    while y:
        r=x%y
        x=y
        y=r
    print('x,y的最大公约数为',x)
x=int(input('x='))
y=int(input('y='))
gcd(x,y)