
x=int(input("enter a number"))
if x in range(1, 101):
    print(x,"is in range 1 to 100")
else:
    print(x,"is not in range 1 to 100") 








salary=int(input("enter amount"))
if salary>0:

    if salary<=250000:
        print("no tax")
    elif salary<=500000:
        salary=salary-250000
        salary=(salary*5)/100
        print("salary taxes:",salary)
    elif salary<=1000000:
        salary=salary-250000
        salary=(salary*7)/100
        print("salary taxes:",salary)
    elif salary>1000000:
        salary=salary-250000
        salary=(salary*10)/100
        print("salary taxes:",salary)
else:
    print("enter valid amount")

