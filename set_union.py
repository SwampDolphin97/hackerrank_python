# Enter your code here. Read input from STDIN. Print output to STDOUT
int(raw_input())
n=set(list(map(int,raw_input().split())))
int(raw_input())
m=set(list(map(int,raw_input().split())))
#x=n.union(m)
print len(n.union(m))

