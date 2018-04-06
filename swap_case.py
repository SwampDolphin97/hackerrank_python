def swap_case(s):
    a=''
    for i in s:
        if i.islower()==True:
            a+=i.upper()
        else:
            a+=i.lower()
        
    return a 
