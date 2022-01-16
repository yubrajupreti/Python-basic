class ElectricityBill:
    def __init__(self):
        self.customerId=0
        self.name=" "
        self.unit=0
        self.amount=0

    def input(self):
        self.customerId=int(input("enter the cusotmerid"))  
        self.name=input("enter the name of the customer")
        self.unit=int(input("enter the unit consumed"))
        self.amount=int(input("enter the amount:\t"))
        
    def calc(self):
        if(self.unit<21):
            self.amount=self.unit*7
        elif(self.unit<81):
            self.amount=140+(10*(self.unit-20))
        elif(self.unit<120):
            self.amount=720+(12*(self.unit-80))
        else:
            self.amount=1200+(20*(self.unit-120))

    def display(self):
        print(self.customerId,"\t\t",self.name,"\t\t",self.unit,"\t\t",self.amount)

if __name__ == "__main__":
    bill= ElectricityBill()
    bill.input()
    bill.calc()
    print("id\t\tname\t\tunits\t\tamount")
    bill.display()            