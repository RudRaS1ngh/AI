initial=[7,2,4,5,'9',6,8,3,1]
win=[1,2,3,4,5,6,7,8,'9']
stack=[initial]
visited=[]
state=[]

def up(l2):
    l1=l2.copy()
    ind=l1.index('9')
    if(ind>=3):
        temp=l1[ind]
        l1[ind]=l1[ind-3]
        l1[ind-3]=temp
    return l1

def down(l2):
    l1=l2.copy()
    ind=l1.index('9')
    if(ind<6):
        temp=l1[ind]
        l1[ind]=l1[ind+3]
        l1[ind+3]=temp
    return l1

def left(l2):
    l1=l2.copy()
    ind=l1.index('9')
    if(ind%3!=0):
        l1[ind],l1[ind-1]=l1[ind-1],l1[ind]
    return l1

def right(l2):
    l1=l2.copy()
    ind=l1.index('9')
    if(ind%3!=2):
        l1[ind],l1[ind+1]=l1[ind+1],l1[ind]
    return l1

while stack:
    state=stack.pop()
    
    if state not in visited:
        visited.append(state)
        print("Exploring:", state)
        if(state==win):
            break
        ind=state.index('9')
        if ind>=3:
            l1=up(state)
            if l1 not in visited and l1 not in stack:
                stack.append(l1)
        if ind<6:
            l2=down(state)
            if l2 not in visited and l2 not in stack:
                stack.append(l2)
        if ind%3!=0:
            l3=left(state)
            if l3 not in visited and l3 not in stack:
                stack.append(l3)
        if ind%3!=2:
            l4=right(state)
            if l4 not in visited and l4 not in stack:
                stack.append(l4)
        
print(visited)
