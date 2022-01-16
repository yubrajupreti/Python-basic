salary = 0
stats = "N"
def userIn():
    stats = input("Enter s for Single and c for Couple : ")
    salary  =  int(input("Enter sallary : "))
    return stats,salary

def cal_tax(status, income):
    if status == 'c':
        if income <= 400000:
            total_tax = income * .01
        elif income <= 500000:
            total_tax = (income - 400000) * 0.1 + 4000
        elif income <= 700000:
            total_tax = (income - 500000) * 0.2 + 14000
        elif income <= 2000000:
            total_tax = (income - 700000) * 0.3 + 54000
        else:
            total_tax = (income - 2000000) * 0.36 + 444000
        return total_tax
    else:
        if income <= 450000:
            total_tax = income * .01
        elif income <= 550000:
            total_tax = (income - 450000) * 0.1 + 4500 #
        elif income <= 750000:
            total_tax = (income - 550000) * 0.2 + 14500
        elif income <= 2000000:
            total_tax = (income - 750000) * 0.3 + 54500
        else:
            total_tax = (income - 2000000) * 0.36 + 429500

    return total_tax

def display(tax,income):

    print("Your income per annum is "+str(income))
    print("Your total tax to be paid is "+str(tax))
    d = income - tax
    print(f"Amount after removing tax is {d}")

def main():
   stats,salary = userIn()
   print("The employee is ",stats)
   print("The monthly income is ",salary)
   print("The yearly income is ",salary*12)
   tax = cal_tax(stats,salary)
   display(tax,salary)

main()
