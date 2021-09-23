from person import Person

class Teacher(Person):
    def __init__(self, fname, lname, bdate, phone, email, degree, subject):
        self.degree = degree
        self.subject = subject
        super().__init__(fname, lname, bdate, phone, email)

    def __str__(self) -> str:
        return super().__str__() + f"""Degree: {self.degree}
        Subject: {self.subject}
        """