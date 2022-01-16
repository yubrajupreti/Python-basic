class Rectangle:
    def __init__(self):
        self.length=0
        self.breadth=0

    def format(self,input_length,input_breadth):
        self.length=float(input_length)
        self.breadth=float(input_breadth)

    def get_area(self):
        return self.length*self.breadth


if __name__=="__main__":
    input_length=input("enter the value of length")
    input_breadth= input("enter the value of breadth")
    area=Rectangle()
    area.format(input_length,input_breadth)
    print(area.get_area())          
