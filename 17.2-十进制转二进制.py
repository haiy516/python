#作者：王辉
#日期：2020/3/11
#时间：11:04
def Dec2Bin(x):
    bin=[]
    while x:
        r=x%2
        x=x//2
        bin.append(r)
    bin.reverse()
    return bin
x=int(input('请输入一个大于0的整数：'))
bin1=Dec2Bin(x)
str1=''
for i in bin1:
    str1+=str(i)
print(x,'转化为二进制为:',str1)