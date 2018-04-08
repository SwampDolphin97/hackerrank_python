from itertools import combinations
s=raw_input().split()
str=sorted(s[0])
k=int(s[1])
for i in range(1,k+1):    #printing all possible combinations
    for j in combinations(str,i):           #calculating all possible combinations
        print(''.join(j))                   #printing as characters
    
