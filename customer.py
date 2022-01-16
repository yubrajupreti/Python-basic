type=('A','B', 'C', 'D')
dis_type=(0.25, 0.15, 0.1,0)

def User_input():
    day = []
    unit = []

    stock_day = int(input("How manys days stock info you want to store"))
    cus_id = int(input("customer id => "))
    date = int(input("Date => "))
    for i in range(stock_day):
        days = int(input("day{} - ".format([i + 1])))
        day.append(days)
        unit_price = int(input("unit price{} - ".format([i + 1])))
        unit.append(unit_price)

    return day,unit,stock_day

def Calculate(day=[],unit=[]):
    charge_day=[]
    total_charge=0
    day,unit,stock_day=User_input()
    for i in range(stock_day):
        charge = day[i]*unit[i]
        charge_day.append(charge)
        total_charge=total_charge+charge

    if total_charge<200:
        dis=dis_type[3]*charge
        after_dis=charge-dis
    elif total_charge<401:
        dis=dis_type[2]*charge
        after_dis=charge-dis
    elif total_charge<600:
        dis=dis_type[1]*charge
        after_dis=charge-dis
    else:
        dis=dis_type[0]*charge
        after_dis=charge-dis

    return  dis, after_dis,total_charge,stock_day, charge_day

def display(dis, after_dis, total_charge, stock_day,charge_day=[] ):
    Calculate()
    for i in range(stock_day):

    print("Total charge = " + total_charge)
    print("Discounted price : "+dis)
    print("Price after discount: "+after_dis)







