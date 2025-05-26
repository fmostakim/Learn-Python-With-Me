class Employee:
    language = "Py" # This is a class attributes
    salary = 1200000

mostakim = Employee()
mostakim.name = "Mostakim"  # This is an instance attributes
print(mostakim.name, mostakim.language, mostakim.salary)


tahmid = Employee()
tahmid.name = "Tahmid konar husband "
print(tahmid.name, tahmid.language, tahmid.salary)

# Here name is instance attribute and salary and language  are 
# class attributes as they directly belong to the class

