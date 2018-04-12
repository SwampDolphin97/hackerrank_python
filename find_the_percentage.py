#Inputs
if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    for i in student_marks:
        if(i==query_name):
            avg = 0.0
            counter = 0
            for scores in student_marks[i]:
                avg=avg+scores
                counter=counter+1
            number = avg/counter
            print("%.2f"%number)
