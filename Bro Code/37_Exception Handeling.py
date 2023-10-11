#If declaration was done globally , Value error woudn't have been detected

numerator=int(input("Enter your Numerator "))
denominator=int(input("Enter your Denominator "))
try:
    # numerator=int(input("Enter your Numerator "))
    # denominator=int(input("Enter your Denominator "))
    result=numerator/denominator
    # print(result)
except ZeroDivisionError as e:
    print(e)
    print("You can't devide by zero")
except ValueError as e:
    print(e)
    print("Only values are allowed")
except Exception as e:
    print(e)
    print("Something went wrong! :(")
else:
    print(result)