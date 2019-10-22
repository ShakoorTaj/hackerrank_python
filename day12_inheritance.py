class Person:
    def __init__(self, first_name, last_name, id):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def printPerson(self):
        print("Name: {}, {}".format(self.last_name, self.first_name))
        print("ID: {}".format(self.id))


class Student(Person):
    def __init__(self, first_name, last_name, id, scores):
        self.scores = scores
        Person.__init__(self, first_name, last_name, id)

    def calculate(self):
        avg = sum(self.scores) / len(self.scores)
        if 90 <= avg <= 100:
            return 'O'
        elif 80 <= avg < 90:
            return 'E'
        elif 70 <= avg < 80:
            return 'A'
        elif 55 <= avg < 70:
            return 'P'
        elif 40 <= avg < 55:
            return 'D'
        else: # avg < 40:
            return 'T'


stdobj = Student('ali', 'aktar', 12345, [4,4,4,4])
stdobj.printPerson()
print(stdobj.calculate())
