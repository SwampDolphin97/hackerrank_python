def capitalize(string):
    #str=string.title()
    #return str
    l=string.split(" ")
    a = [i.capitalize() for i in l]       
    return " ".join(a)
