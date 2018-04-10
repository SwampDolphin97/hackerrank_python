
int(raw_input())
n=set(list(map(int,raw_input().split())))
int(raw_input())
m=set(list(map(int,raw_input().split())))
print  len(n.symmetric_difference(m))
