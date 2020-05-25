#作者：王辉
#日期：2020/3/12
#时间：20:12
def strclassify(str1):
    alpha=0
    number=0
    space=0
    others=0
    for i in range(len(str1)):
        if str1[i].isalpha():
            alpha+=1
        elif str1[i].isdigit():
            number+=1
        elif str1[i].isspace():
            space+=1
        else:
            others+=1
    print(str1,'中字母的个数为：',alpha)
    print(str1, '中数字的个数为：', number)
    print(str1, '中空格的个数为：', space)
    print(str1, '中其他字符的个数为：', others)
str1=input('请输入要分类的字符串：')
strclassify(str1)