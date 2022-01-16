
class MYPLACE:

   def __init__(self,pCode=0, pName = "", pPop=0, pKM=0, pDensity=0):

    self.pCode = pCode
    self.pName = pName
    self.pPop = pPop
    self.pKM = pKM
    self.pDensity = pDensity

   def P_CalDen(self):

        self.pDensity = self.pPop / self.pKM

   def P_Record(self):

       self.pName = input("Enter Name : ")
       self.pCode = int(input("Enter Code : "))
       self.pPop = int(input("Enter Population : "))
       self.pKM = int(input("Enter KM : "))
       self.P_CalDen()
       self.P_See()


   def P_See(self):

       print("The Name of the place is ", self.pName)
       print("The Code is :", self.pCode)
       print("Population : ", self.pPop)
       print("Km : ", self.pKM)
       print("Density :", self.pDensity)
       if (self.pDensity > 15000):
           print("Highly Populated Area")

p1 = MYPLACE()
p1.P_Record()
