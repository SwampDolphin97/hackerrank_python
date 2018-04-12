#Input
list = []
numlist = []
cases = int(input())
for _ in range(cases):
    name = raw_input()
    number = float(input())
    templist = [name,number]
    list.append(templist)

for name,number in list:
    numlist.append(number)
x = (min(numlist))

while(x==min(numlist)):
    numlist.remove(x)

for name,number in sorted(list):
    if(number==min(numlist)):
        print name
    
