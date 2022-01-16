import math

def bmi_calculator(weights, heights):
    weight_kg = weights*0.45359237
    height_meter = heights*0.0254
    print ("Your height in meter : ",height_meter)
    print("Your weight in kg  :",weight_kg)
    bmi = weight_kg/ (math.pow((height_meter),2))
    print ("Your BMI is :",bmi)
    
    if(bmi>18.5):

        print("According to your BMI you are categories : Underweight")
    elif(bmi>24.9 and bmi<18.5):

        print("According to your BMI you are categories : Normal")
    elif(bmi>25.0 and bmi<29.9):

        print("According to your BMI you are categories :  overweight")
    elif(bmi>30.0):

        print("According to your BMI you are categories : obese")

def main():

    print("Welcome to BMI calculator")
    print(" 1 Pound = 0.45359237 and 1 inch = 0.0254 meters")
    weights_pounds = float(input("Enter weight in pounds = "))
    heights_inches = float(input("Enter height in inches = "))
    bmi_calculator(weights_pounds, heights_inches)

main()