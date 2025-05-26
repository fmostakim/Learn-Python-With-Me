class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000

mostakim = Employee()
mostakim.language = "JavsScript"  #This is an instance attribute
print(mostakim.language, mostakim.salary) 