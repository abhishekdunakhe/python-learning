from random import randint

class TrainTicket:

    def __init__(self,trainNo):
        self.trainNo = trainNo
        
    def book(self, fro, to):
        print(f"The train {self.trainNo} is book from {fro} to {to}.")

    def get_sts(self):
        print(f"The train {self.trainNo} is running on time.")

    def get_fare(self, fro, to):
        print(f"Ticket fair in train no: {self.trainNo} from {fro} to {to} is {randint(222, 55555)}.")

t = TrainTicket(1299)

t.book("pune", "Delhi")
t.get_sts()
t.get_fare("pune", "Baramati")
