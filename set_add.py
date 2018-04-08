# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(raw_input())
#l=raw_input().split()
l=[]
for i in range(n):
    l.append(raw_input())
s=set(l)
print len(s)
