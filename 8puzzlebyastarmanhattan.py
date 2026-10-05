initial=[2,8,3,1,6,4,7,'9',5]
win=[1,2,3,8,'9',4,7,6,5]

visited=[]
state=[]

def mismatch(s1):
    hn=0
    for i in range(9):
        if s1[i]!='9':
            if(s1[i]!=win[i]):
                srow=i//3
                scol=i%3
                cor=win.index(s1[i])
                crow=cor//3
                ccol=cor%3
                if crow>srow:
                    x=crow-srow
                else:
                    x=srow-crow
                if ccol>scol:
                    y=ccol-scol
                else:
                    y=scol-ccol
                hn+=x+y
                
    return hn

    
def up(l2):
    l1=l2[2].copy()
    ind=l1.index('9')
    if(ind>=3):
        temp=l1[ind]
        l1[ind]=l1[ind-3]
        l1[ind-3]=temp
    hr=mismatch(l1)
    g=l2[1]+1
    f=g+hr
    return (f,g,l1)

def down(l2):
    l1=l2[2].copy()
    ind=l1.index('9')
    if(ind<6):
        temp=l1[ind]
        l1[ind]=l1[ind+3]
        l1[ind+3]=temp
    hr=mismatch(l1)
    g=l2[1]+1
    f=g+hr
    return (f,g,l1)

def left(l2):
    l1=l2[2].copy()
    ind=l1.index('9')
    if(ind%3!=0):
        l1[ind],l1[ind-1]=l1[ind-1],l1[ind]
    hr=mismatch(l1)
    g=l2[1]+1
    f=g+hr
    return (f,g,l1)

def right(l2):
    l1=l2[2].copy()
    ind=l1.index('9')
    if(ind%3!=2):
        l1[ind],l1[ind+1]=l1[ind+1],l1[ind]
    hr=mismatch(l1)
    g=l2[1]+1
    f=g+hr
    return (f,g,l1)

stack=[(mismatch(initial),0,initial)]

while stack:
    h_stack=[]
    for i in stack:
        h_stack.append(i[0])
    ind1=h_stack.index(min(h_stack))
    state=stack[ind1]
    
    if state[2] not in visited:
        visited.append(state[2])
        #print("Exploring:", state)
        if(state[2]==win):
            break
        ind=state[2].index('9')
        if ind>=3:
            f1,g1,l1=up(state)
            if l1 not in visited:
                stack.append((f1,g1,l1))
        if ind<6:
            f2,g2,l2=down(state)
            if l2 not in visited:
                stack.append((f2,g2,l2))
        if ind%3!=0:
            f3,g3,l3=left(state)
            if l3 not in visited:
                stack.append((f3,g3,l3))
        if ind%3!=2:
            f4,g4,l4=right(state)
            if l4 not in visited:
                stack.append((f4,g4,l4))
        stack.remove(state)
        
print(visited)
