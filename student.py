from person import Person

class Student(Person):
    def __init__(self, fname, lname, bdate, phone, email, score):
        self.score = score
        self.grade = self.__getGrade(score)
        super().__init__(fname, lname, bdate, phone, email)

    def __getGrade(self, score):
        if score >= 90:
            return "A"
        if score >= 80:
            return "B"
        if score >= 70:
            return "C"
        if score >= 60:
            return "D"
        else:
            return "F"

    def __str__(self) -> str:
        return super().__str__() + f"""Score: {self.score}
        Grade: {self.grade}
        """
