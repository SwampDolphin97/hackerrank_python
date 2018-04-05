def split_and_join(line):
    # write your code here
    s=line.split(" ")
    a=""
    for i in s:
        a = "-".join(s)
    return a
