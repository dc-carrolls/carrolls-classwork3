student_marks = "bob",75,"garry",55,"dave",87,"trevor",73
grades = {80:"A*",70:"A",60:"B",50:"C"}
print(student_marks[0])
def assignGrades(marks,grades):
    for n in range(0,len(marks),2):
        