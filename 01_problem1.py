from encodings.punycode import T


class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = Programmer("Mostakim", 1200000, 2430197)
print(p.name, p.salary, p.pin, p.company)

t = Programmer("Tahmid", 1200000, 2430199)     
print(t.name, t.salary, t.pin, t.company)