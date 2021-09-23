from teacher import Teacher
from student import Student


class LMS:
    def __init__(self):
        self.students = []
        self.teachers = []

    def addStudent(self, student: Student):
        self.students.append(student)

    def addTeacher(self, teacher: Teacher):
        self.teachers.append(teacher)

    def search(self, object: str):
        sf = 0
        sl = 0
        results = []
        for student in self.students:
            for i in range(len(object)):
                sf = 0
                sl = 0
                if object[i] == student.firstname[i]:
                    sf = 1
                    continue
                else: 
                    sf = 0
                    break
            for i in range(len(object)):
                if object[i] == student.lastname[i]:
                    sl = 1
                    continue
                else: 
                    sl = 0
                    break
            
            if sf == 1 or sl == 1:
                results.append(student)
                continue
        for teacher in self.teachers:
            for i in range(len(object)):
                sf = 0
                sl = 0
                if object[i] == teacher.firstname[i]:
                    sf = 1
                    continue
                else: 
                    sf = 0
                    break
            for i in range(len(object)):
                if object[i] == teacher.lastname[i]:
                    sl = 1
                    continue
                else: 
                    sl = 0
                    break
            
            if sf == 1 or sl == 1:
                results.append(teacher)
                continue
        if len(results) > 0:
            for result in results:
                print(result)
        else:
            print("Not found")
            


    def getStudents(self):
        arr = []
        for st in self.students:
            arr.append(f'{st.firstname} {st.lastname}')
        return arr

    def getTeachers(self):
        arr = []
        for t in self.teachers:
            arr.append(f'{t.firstname} {t.lastname}')
        return arr



st2 = Student("Nafisa", "O'taboyeva", 2002, 65464, "asdf@dsf", 95)
najottalim = LMS()
st3 = Student("Gulbahor", "Mustafayeva", 1999, 65464, "asdf@dsf", 85)
st1 = Student("Muhlisa", "Qudratova", 2000, 65464, "asdf@dsf", 75)
st4 = Student("Lobar", "O'taboyeva", 2004, 65464, "asdf@dsf", 95)

t1 = Teacher("Dilrabo", "Mustafayeva", 1971, 65464, "asdf@dsf",'oliy','matem')

najottalim.addStudent(st2)
najottalim.addStudent(st3)
najottalim.addStudent(st1)
najottalim.addStudent(st4)
najottalim.addTeacher(t1)
# print(st2)

# print(najottalim.students[0])
b = input()
najottalim.search(b)
print(najottalim.getStudents())
print(najottalim.getTeachers())
