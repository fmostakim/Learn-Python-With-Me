from random import randint

class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo
        

    def book(mostakim, fro, to):
        print(f"Ticket is booked in train no: {mostakim.trainNo} from {fro} to {to} ")


    def getStasus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")

t = Train(123999)
t.book("Khulna", "Dhaka")
t.getStasus()
t.getFare("Khulna", "Dhaka")