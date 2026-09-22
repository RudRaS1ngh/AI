a=int(input("A:"))
b=int(input("B:"))
agent=int(input("Loc:"))
state=[a,b]
def vc_reflex(st,loc):
    if st[loc]==1:
        print("Clean state ",loc)
        st[loc]=0
    else:
        print("State ",loc,"already clean.")
        if loc==0:
            loc=1
        else:
            loc=0
    return loc
flag=1
while(flag):
    agent=vc_reflex(state,agent)
    if state[0]==0 and state[1]==0:
        print("Both states are clean.")
        flag=0
