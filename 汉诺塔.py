#作者：王辉
#日期：2020/3/14
#时间：21:55
def hanoi(n,x,y,z):
    if n==1:
        print(x,'-->',z)
    else:
        hanoi(n-1,x,z,y)
        print(x,'-->',z)
        hanoi(n-1,y,x,z)
n=int(input('请输入汉诺塔的层数：'))
hanoi(n,'X','Y','Z')
####当汉诺塔为n层时，最少的移动次数为:2^n-1