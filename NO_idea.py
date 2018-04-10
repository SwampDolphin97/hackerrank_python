# Enter your code here. Read input from STDIN. Print output to STDOUT
#n=int(raw_input())
#m=int(raw_input())
#a=[]
#for i in range(n):
a=raw_input().split()
#a.append(raw_input())
n = map(int, raw_input().split())
x=raw_input().split()
y=raw_input().split()
A=set(list(map(int,x)))
B=set(list(map(int,y)))
happy=0
for i in n:
    if i in A:
        happy+=1
    elif i in B:
        happy-=1
print happy
    
    
