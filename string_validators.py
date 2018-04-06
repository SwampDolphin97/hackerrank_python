if __name__ == '__main__':
    s = raw_input()
    a=0
    b=0
    l=0
    u=0
    x=0
    #print s.isalnum()
    for c in s:
        if c.isalnum():
            x+=1
        if c.isalpha():
            a+=1
        if c.isdigit():
            b+=1
        if c.islower():
            l+=1
        if c.isupper():
            u+=1
    if x>0:
        print True
    else:
        print False
    if a>0:
        print True
    else:
        print False
    if b>0:
        print True
    else:
        print False
    if l>0:
        print True
    else:
        print False
    if u>0:
        print True
    else:
        print False
    
   
