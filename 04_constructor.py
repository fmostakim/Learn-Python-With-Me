



class Employee:
    language = "Python" #This is a class attributes
    salary = 1200000

    def __init__(self, name, salary, language):  # dunder method which is automatically called
        self.name = name
        self.language = language
        self.salary = salary

        print("I am creating an object")

    def getinfo(self):  #ekhane jodi bracket na ditam tahole function call korar somoy nam dile error! dito

        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

mostakim = Employee("Mostakim", 1300000, "Javascript")

mostakim.name = "Mostakim"
print(mostakim.name, mostakim.salary, mostakim.language)

# tahmid = Employee()
