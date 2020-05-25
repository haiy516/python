#求阶梯数
x=1
while x<200:
    x+=1
    if (x%2==1)and(x%3==2)and(x%4==3)and(x%5==4)and(x%6==5)and(x%7==0):
        print(x)