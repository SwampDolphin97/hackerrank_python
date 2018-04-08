from itertools import product
A=list(map(int,raw_input().split()))   #input of a list of integers
B=list(map(int,raw_input().split()))
#print product(A,B)
for i in product(A, B): #all elements in the returned list needs to be printed
    print i,
