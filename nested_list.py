list=[]
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    l=[name,score]
    list.append(l)
    
min=99999    
for i in list:
    name=i[0]
    score=i[1]
    if(min<score):
        min=score
    
for i in list:
    if(i[1]==min):
        print(i[0])
