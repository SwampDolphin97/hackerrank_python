A=set(list(map(int,raw_input().split())))
x=int(raw_input())
c=0
for i in range(x):
    B=set(list(map(int,raw_input().split())))
    s=0
    for i in A:
        if i in B:
            s+=1
    if s==len(B):#as A needs to be superset
        c+=1
if c==x:
    print True
else:
    print False
