x=input()
for i in range(x):
    int(raw_input())
    A=set(list(map(int,raw_input().split())))
    int(raw_input())
    B=set(list(map(int,raw_input().split())))
    c=0
    for i in A:
        if i in B:
            c+=1
    if c==len(A):
        print True
    else:
        print False
        
