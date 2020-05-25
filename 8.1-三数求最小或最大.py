#三者取最小或最大
x=int(input('请输入第一个数字:'))
y=int(input('请输入第二个数字:'))
z=int(input('请输入第三个数字:'))
min=x if (x<y and x<z)else(y if y<z else z)
max=x if (x>y and x>z)else(y if y>z else z)
print('x,y,z 中最小的是',min)
print('x,y,z 中最大的是',max)