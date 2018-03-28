cases = input()
while cases is not 0:
    ph_num = raw_input()
    try:
        conversion = int(ph_num)
        if (ph_num[0] == '7' or ph_num[0] == '8' or ph_num[0] == '9') and len(ph_num) is 10:
            print("YES")
        else:
            print("NO")
    except ValueError:
        print("NO")
    cases=cases-1
