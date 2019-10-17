x = 1
while(x<4):
    print(x)
    x+=1

y = [4,5,6]
for i in y:
    print(i)

for j in range(7,40,3):
    if(j==16):
        break
    '''break makes the sequence to end
        continue skips the particular point
            pass is just for syntactically correct statement
                '''
    for k in range(j,j+3):
        print(k)