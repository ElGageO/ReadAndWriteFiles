import csv

students = open('Student_Scores.csv', 'r')
students_file = csv.reader(students, delimiter = ',')

avgs = open('student_avg.csv', 'w', newline = '')
avgs_file = csv.writer(avgs, delimiter = ',')

for student in students_file:
    name = student[0]
    score1 = int(student[1])
    score2 = int(student[2])
    score3 = int(student[3])

    avg = round((score1 + score2 + score3) / 3, 2)
    
    avg_list = [name, avg]
    avgs_file.writerow(avg_list)

students.close()
