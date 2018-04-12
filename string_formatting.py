def print_formatted(number):
    output_string = ""
    width = len(str("{0:b}".format(number)))
    for i in range(1,number+1):
        output_string = str(i).rjust(width," ") + " " + str("{0:o}".format(i)).rjust(width," ") + " " + str("{0:x}".format(i)).rjust(width," ").upper() + " " + str("{0:b}".format(i).rjust(width," "))
        print output_string
    return 0
