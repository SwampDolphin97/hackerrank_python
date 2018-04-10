from itertools import permutations
s=raw_input().split()         #splitting the input to list and integer
str=sorted(s[0])              #in sorted order as per the question
k=int(s[1])
#print k
#print list(permutations(str,k))
for i in permutations(str,k):
    print(''.join(i))         #to avoid printing in the form of list
