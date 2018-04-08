int(raw_input())
N=raw_input().split()#splitting the input values
Nint=set(list(map(int,N)) ) #using map to convert all values of list into string

int(raw_input())
M=raw_input().split()
Mint=set(list(map(int,M)))

res=[]
for i in list(Nint.difference(Mint)):#traversing the nint array which comntains converted string values of set N and finding the difference by comparing set M and N using difference method
    res.append(i)
for j in list(Mint.difference(Nint)):
    res.append(j)
for k in sorted(res):
    print k


