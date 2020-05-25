#作者：王辉
#日期：2020/3/12
#时间：17:31
def findstr(decstr,substr):
    count=0
    if substr not in decstr:
        print(decstr,'中不存在',substr)
    else:
        for i in range((len(decstr)-1)):
            if decstr[i]==substr[0] and decstr[i+1]==substr[1]:
                count+=1
    print('字符串',substr,'在字符串',decstr,'中出现的次数为：',count)
decstr=input('请输入原字符串：')
substr=input('请输入要查找的两个字符串：')
findstr(decstr,substr)