from itertools import combinations_with_replacement
s=raw_input().split()
str=sorted(s[0])
k=int(s[1])
for i in combinations_with_replacement(str,k):
    print(''.join(i))
