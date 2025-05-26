class Employee:
    language = "Python" #This is a class attributes
    salary = 1200000

    def getinfo(self):  #ekhane jodi bracket na ditam tahole function call korar somoy nam dile error! dito

        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

mostakim = Employee()
mostakim.greet()  # This instance attribute .something diye instance attibute banai

mostakim.getinfo()
# Employee.getinfo(mostakim)
