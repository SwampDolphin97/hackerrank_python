#Input
list = []
cases = input()
for _ in range(cases):
    list.append(raw_input())

cases = input()
for _ in range(cases):
    value = raw_input()
    counter = 0
    for item in list:
        if (item==value):
            counter=counter+1
    print counter

