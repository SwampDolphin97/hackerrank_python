length, width = map(int, raw_input().split(" "))
str = ".|."
temp = str
counter = 1


#Top side
for i in range(0,length//2):
    counter+=2
    print(temp.center(width,'-'))
    temp=str*counter

#Middle Side
print("WELCOME".center(width,'-'))
counter-=2

#Bottom Side
for i in range(length//2+1,length):
    temp=str*counter
    print(temp.center(width,'-'))
    counter-=2
