#作者：王辉
#日期：2020/3/13
#时间：21:31
str1='12332\n1aaa'
print(str1)
list1=[]
for each in str1:
    if each not in list1:
        if each=='\n':
            print('\\n',str1.count(each))
        else:
            print(each, str1.count(each))
    list1.append(each)

