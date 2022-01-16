from threading import Timer
import random
def main():
    timeout = 15
    t = Timer(timeout, print, ['Sorry, times up'])
    t.start()
    prompt = "You have %d seconds to choose the correct answer...\n" % timeout
    n = random.randint(3,10)
    print(n)
    print("Enter any", n," lenght word in 15 seconds")
    print("Your timer starts now")  
    answer = input(prompt)
    userInp(answer)
    t.cancel()
def userInp(word):
    words_vals = {1: ["A","E","I","O","U","L","N","R","S","T"],
             2: ["D","G"],
             3: ["B","C","M","P"],
             4: ["F","H","V","W","Y"],
             5: ["K"],
             8: ["J","X"],
             10:["Q","Z"]
    }
    count = 0
    if word.isalpha():
        print("The word is ",word)
        for char in word:
            if char.islower():
                char = char.upper()
            list_of_keys = [key for key, list_of_values in words_vals.items() if char in list_of_values] 
            if list_of_keys:
                count += list_of_keys[0]
            else:
                print('Value does not exist in the dictionary')
            
    else: 
        print("Please enter only letters")
    print("Total letter counts in word is :",count) 
main()
