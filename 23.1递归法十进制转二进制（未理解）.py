#作者：王辉
#日期：2020/3/15
#时间：13:23
def Dec2Bin(x):
    bin=''
    if x:
        bin=Dec2Bin(x//2)
        return bin+str(x%2)
    else:
        return bin
print(Dec2Bin(0))