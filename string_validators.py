if __name__ == '__main__':
    s = raw_input()
    flagalnum = flagalpha = flagdigit = flaglower = flagupper = 0
    for i in s:
        if i.isalnum():
            flagalnum = 1
        if i.isalpha():
            flagalpha = 1
        if i.isdigit():
            flagdigit = 1
        if i.islower():
            flaglower = 1
        if i.isupper():
            flagupper = 1
    print("True" if flagalnum else "False")
    print("True" if flagalpha else "False")
    print("True" if flagdigit else "False")
    print("True" if flaglower else "False")
    print("True" if flagupper else "False")
