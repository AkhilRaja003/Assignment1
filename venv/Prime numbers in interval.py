x = int(input("Give initial value:"))
y = int(input("Give final value:"))
for i in range(x,y+1):
    loop = 0
    for j in range(1,i+1):
        if i%j==0:
         loop=loop+1
    if loop==2:
        print(i)