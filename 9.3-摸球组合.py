#红3黄3绿6，摸出8个，求摸出的组合情况
print('red\tyellow\tblue')
for red in range(0,4):
    for yellow in range(0,4):
        for green in range(2,7):
            if red+yellow+green==8:
                print(red, '\t', yellow, '\t', green)
