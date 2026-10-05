initial=[2,8,3,1,6,4,7,'9',5]
win=[1,2,3,8,'9',4,7,6,5]
stack=[(0,initial)]
visited=[]
state=[]

def mismatch(s1):
    hn=0
    for i in range(9):
        if(s1[i]!=win[i]):
            hn+=1
    return hn

    
def up(l2):
    l1=l2[1].copy()
    ind=l1.index('9')
    if(ind>=3):
        temp=l1[ind]
        l1[ind]=l1[ind-3]
        l1[ind-3]=temp
    hr=mismatch(l1)
    return (hr,l1)

def down(l2):
    l1=l2[1].copy()
    ind=l1.index('9')
    if(ind<6):
        temp=l1[ind]
        l1[ind]=l1[ind+3]
        l1[ind+3]=temp
    hr=mismatch(l1)
    return (hr,l1)

def left(l2):
    l1=l2[1].copy()
    ind=l1.index('9')
    if(ind%3!=0):
        l1[ind],l1[ind-1]=l1[ind-1],l1[ind]
    hr=mismatch(l1)
    return (hr,l1)

def right(l2):
    l1=l2[1].copy()
    ind=l1.index('9')
    if(ind%3!=2):
        l1[ind],l1[ind+1]=l1[ind+1],l1[ind]
    hr=mismatch(l1)
    return (hr,l1)

while stack:
    h_stack=[]
    for i in stack:
        h_stack.append(i[0])
    ind1=h_stack.index(min(h_stack))
    state=stack[ind1]
    
    if state[1] not in visited:
        visited.append(state[1])
        #print("Exploring:", state)
        if(state[1]==win):
            break
        ind=state[1].index('9')
        if ind>=3:
            f1,l1=up(state)
            if l1 not in visited and l1 not in stack:
                stack.append((f1,l1))
        if ind<6:
            f2,l2=down(state)
            if l2 not in visited and l2 not in stack:
                stack.append((f2,l2))
        if ind%3!=0:
            f3,l3=left(state)
            if l3 not in visited and l3 not in stack:
                stack.append((f3,l3))
        if ind%3!=2:
            f4,l4=right(state)
            if l4 not in visited and l4 not in stack:
                stack.append((f4,l4))
        stack.remove(state)
        
print(visited)
