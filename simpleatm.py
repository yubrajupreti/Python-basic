import random
import time


def atm():
    print("enter the card")
    code=int(input("enter the pin code"))
    atm=[1111,2222,3333]


    if code in atm:
        if code==1111:
            blnc=10000
            
        elif code==2222:
            blnc=11000
           
        elif code==3333:
            blnc=12000
            
        else:
            blnc=0
            
        print("choose your transaction\n")
        print("1.balance inqury")
        print("2.fast cash")
        print("3.withdraw")
        print("4.exit")
        selection=int(input("enter the process from 1 to 4"))
        
        s=selection
        if s==1:
            print("     Processing...")
            time.sleep(2)
            print(blnc)
            
        elif s==2:
            print("     Processing...")
            time.sleep(2) 
            print("1.1000")
            print("2.500")
            print("3.1500")
            print("4.2000")
            amt=int(input("press 1-4 for transaction"))
            if amt==1:
                print("     Processing...")
                time.sleep(4)
                money=1000
                if blnc>=money:
                    print("please collect your cash")
                else:
                    print("not enough money")     
            elif amt==2:
                print("     Processing...")
                time.sleep(4)
                money=500
                if blnc>=money:
                    print("please collect your cash")
                    blnc=blnc-money
                    print("your balance after transaction is ",blnc)
                else:
                    print("not enough money")     
            elif amt==3:
                print("     Processing...")
                time.sleep(4)
                money=1500
                if blnc>=money:
                    print("please collect your cash") 
                    blnc=blnc-money
                    print("your balance after transaction is ",blnc)
                else:
                    print("not enough money")     
            elif amt==4:
                print("     Processing...")
                time.sleep(4)
                money=2000
                if blnc>=money:
                    print("please collect your cash")
                    blnc=blnc-money
                    print("your balance after transaction is ",blnc)                   
                else:
                    print("not enough money")
            else:
                print("invalid input.")

        elif s==3:
            print("     Processing...")
            time.sleep(3)
            amo=int(input("enter your withdraw amount"))
            print("     Processing...")
            time.sleep(4)
            if blnc>=amo:
                print("please collect your cash")
                blnc=blnc-amo
                print("your balance after transaction is ",blnc)
            else:
                print("not enough balance")

        elif s==4:
            print("     Processing...")
            time.sleep(3)
            c=input("press a number to terminate")
        else:
            print("     Processing...")
            time.sleep(4)
            print("not valid input")    

                    
atm()




        
