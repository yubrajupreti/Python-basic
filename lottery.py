import random

def rand(start,end):
    number=random.randint(start, end)
    return number


def user():
    while True:
        num=int(input("Enter the two digit number for lottery "))
        str_num=str(num)
        if len(str_num)>2:
            print("Please enter two digit number. Other are invalid")
            continue

        else:
            break
    return num



def main():
    lottery_number=rand(10,99)
    user_number=user()
    print(lottery_number)
    print(user_number)
    lottery_tens=lottery_number//10
    lottery_ones=lottery_number%10
    user_tens=user_number//10
    user_ones=user_number%10



    if lottery_number==user_number:
        print("Congratulation! You are able to win $10,000")

    elif lottery_ones==user_tens and lottery_tens==user_ones:
        print("Congratulation! You are able to win $3,000")

    elif lottery_tens==user_ones or lottery_tens==user_tens or lottery_ones==user_tens or lottery_ones== user_ones:
        print("Congratulation! You are able to win $1,000")

    else:
        print("NO WIN")



main()

