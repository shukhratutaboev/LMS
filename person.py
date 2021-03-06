class Person:
    def __init__(self, fname, lname, bdate, phone, email):
        self.id = ''
        self.firstname = fname
        self.lastname = lname
        self.birthdate = bdate
        self.phone = phone
        self.email = email

    def __str__(self) -> str:
        return f"""
        ID: {self.id}
        Firstname: {self.firstname}
        Lastname: {self.lastname}
        Birthdate: {self.birthdate}
        Phone: {self.phone}
        Email: {self.email}
        """