def maximum(num1,num2):
  if(num1>num2):
    return num1
  else:
    return num2


if __name__=='__main__':
  num1=int(input("enter the Ist number "))
  num2=int(input("enter the 2nd number "))
  greater = maximum(num1,num2)
  print("The largest number={0}".format(greater))
