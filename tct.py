import random
grid=[0,0,0,0,0,0,0,0,0]
win=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
moves=0
flag=True

while(flag):
    i=int(input("Enter cell:"))

    grid[i-1]="X"
    moves+=1
    empty=[]
    for (a,b,c) in win:
        if grid[a]=="X" and grid[b]=="X" and grid[c]=="X":
            print("Won")
            flag=False
            break
    if not flag:
        break
    if moves==9:
        print("Draw")
        break
    for m in range(0,9,1):
        if grid[m]==0:
            empty.append(m)

    j=random.choice(empty)
    grid[j]="O"
    moves+=1
    print(grid[0:3])
    print(grid[3:6])
    print(grid[6:9])
    for (a,b,c) in win:
        if grid[a]=="O" and grid[b]=="O" and grid[c]=="O":
            print("Lost")
            flag=False
            break
    if not flag:
        break
    
    
    
    
    
