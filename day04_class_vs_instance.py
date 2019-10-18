class Person:
    age = 0  # instance variable

    def __init__(self, initialAge):
        if initialAge <= 0:
            self.age = 0
            print('Age is not valid, setting age to 0.')
        else:
            self.age = initialAge

    def amIOld(self):
        if self.age < 13:
            print('You are young.')
        elif 13 <= self.age < 18:
            print('You are a teenager.')
        else:
            print('You are old.')

    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1


t = int(input())