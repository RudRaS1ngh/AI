initial=[7,2,5,1,6,4,'9',3,8]
win=[1,2,3,4,5,6,7,8,'9']
stack=[initial]
visited=[]
state=[]

def up(l2):
    l1=l2
    ind=l1.index('9')
    if(ind<3):
        temp=l1[ind]
        l1[ind]=l1[ind+6]
        l1[ind+6]=temp
    else:
        temp=l1[ind]
        l1[ind]=l1[ind-3]
        l1[ind-3]=temp
    return l1

def down(l2):
    l1=l2
    ind=l1.index('9')
    if(ind>5):
        temp=l1[ind]
        l1[ind]=l1[ind-6]
        l1[ind-6]=temp
    else:
        temp=l1[ind]
        l1[ind]=l1[ind+3]
        l1[ind+3]=temp
    return l1

def left(l1):
    ind=l1.index('9')
    if(ind%3==0):
        l1[ind],l1[ind+2]=l1[ind+2],l1[ind]
    else:
        l1[ind],l1[ind-1]=l1[ind-1],l1[ind]
    return l1

def right(l1):
    ind=l1.index('9')
    if(ind in [2,5,8]):
        l1[ind],l1[ind-2]=l1[ind-2],l1[ind]
    else:
        l1[ind],l1[ind+1]=l1[ind+1],l1[ind]
    return l1

while(state!=win):
    state=stack.pop()
    print(state)
    if state not in visited:
        visited.append(state)
        l1=up(state)
        stack.append(l1)
        print(stack)
        l2=down(state)
        stack.append(l2)
        print(stack)
        l3=left(state)
        stack.append(l3)
        l4=right(state)
        stack.append(l4)
        
        print(visited)
        print(stack)
print(visited)
