import random

class GuessNumber:
    def __init__(self,given_range=100):
        self.result=random.randint(1,given_range)

    def guess(self, input_number=0):
        if input_number==self.result:
            return "correct"

        elif(input_number>self.result):
            return "its bigger"

        else:
            return "its smaller"

if __name__ == "__main__":
    while True:
        try:
            given_range = int(input("please enter the number larger than 0"))
            if (given_range <= 0):
                print("please key in number ")
                continue
            break
        except:
            print("please key in a valid number ")
        guessnumber =GuessNumber(given_range)
        answer= guessnumber.guess()
        m=int(input("please enter the valid turn you think you can finish "))
        n=0
        while answer!="correct":
            n+=1
            input_number = int(input("please put yours guess <%d:" %given_range))
            answer = guessnumber.guess(input_number)
            print(answer)

        if n<m:
            print("great job,you are smart!")
        else:
            print ("good u need to plsy more")

            
                        