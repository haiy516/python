#作者：王辉
#日期：2020/3/14
#时间：16:25
def fib(n):
    if n==1:
        list1=[1]
    elif n==2:
        list1=[1,1]
    else:
        list1=[1,1]
        for i in range(3,n+1):
            temp=list1[i-2]+list1[i-3]
            list1.append(temp)
    return list1
n=int(input('请输入一个正整数：'))
result=fib(n)
print('fibonacci数列的前',n,'项为：',result)
