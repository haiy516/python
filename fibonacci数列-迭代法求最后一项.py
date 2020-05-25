#作者：王辉
#日期：2020/3/14
#时间：17:58
def fib(n):
    a1=a2=1
    if n==1 or n==2:
        a3=1
    else:
        while n>2:
            a3=a1+a2
            a1=a2
            a2=a3
            n-=1
    return a3
n=int(input('请输入一个正整数：'))
An=fib(n)
print('An=%d'%An)