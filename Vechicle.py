class Vechicle:
    def __init__(self,number_of_wheels,types_of_tank,seating_capacity,velocity):
        self.number_of_wheels= number_of_wheels
        self.type_of_tank=types_of_tank  
        self.seating_capacity=seating_capacity
        self.velocity=velocity
    def set_number_of_wheels(self,number=6):
        self.number_of_wheels=number
    def get_number_of_wheels(self):
        return self.number_of_wheels
    def sound(self,noise="ewwwww"):
        print (noise)


if __name__=="__main__":
    telsa=Vechicle(4,"electrick",6,90)
    print(telsa.number_of_wheels) 
    telsa.set_number_of_wheels(10)
    print(telsa.get_number_of_wheels())
    telsa.sound("weeeeeeee")               
