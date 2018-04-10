input();  
l=raw_input().split();  
s1=set();  
s2=set(); 
for i in l:
    if  i in s1: 
        s2.add(i);#to store duplicate values
    else:
        s1.add(i);#to store unique values
s3=s1.difference(s2);#to find out once occuring value
print list(s3)[0];#to print just the value and not the list
