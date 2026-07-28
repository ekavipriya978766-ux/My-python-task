try:
    age=int(input("enter the age"))
    print(age)
except ValueError:
    print("please enter a valid number")






try:
     a=int(input("enter the number"))
     b=int(input("enter the number"))
     print(a/b)
except ZeroDivisionError:
        print("please enter the valid number")