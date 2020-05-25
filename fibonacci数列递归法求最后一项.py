#作者：王辉
#日期：2020/3/14
#时间：18:15
#a(n)=a(n-1)+a(n-2)
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        An=fib(n-1)+fib(n-2)
        return An
n=int(input('请输入一个整数：'))
result=fib(n)
print(result)