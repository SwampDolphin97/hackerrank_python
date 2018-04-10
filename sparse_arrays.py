#input
cases=int(input())
l=[]
for _ in range(cases):
    str=raw_input()
    l.append(str)
cases=int(input())
for _ in range(cases):
    str=raw_input()
    c=0
    for item in l:
        if(str==item):
            c+=1
    print c 
