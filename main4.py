from tool.utility import is_even,is_odd,maximum,minimum,average,reverse_string,count_vowels,fahrenheit_to_celsius,celsius_to_fahrenheit,kg_to_pounds,pounds_to_kg,is_palindrome
try:
    print("1,is_even")
    print("2,is_odd")
    print("3,maximum")
    print("4,minimum")
    print("5,average")
    print("6,reverse_string")
    print("7,count_vowels")
    print("8,fahrenheit_to_celsius")
    print("9,celsius_to_fahrenheit")
    print("10,kg_to_pounds")
    print("11,pounds_to_kg")
    print("12,is_palindrome")
    print("13,exit")
    choice=int(input("enter the choice"))
    if choice==1:
        print(is_even(n=int(input("Enter a number: "))))
    elif choice==2:
        print(is_odd(n=int(input("Enter a number: "))))
    elif choice==3:
        print(maximum(a=int(input("Enter the first number:")), b=int(input("Enter the second number: "))))
    elif choice==4:
        print(minimum(a=int(input("Enter the first number:")), b=int(input("Enter the second number: "))))
    elif choice==5:
        print(average(a=int(input("Enter the first number:")), b=int(input("Enter the second number: "))))
    elif choice==6:
        print(reverse_string(text=input("Enter a string:")))
    elif choice==7:
        print(count_vowels(text=input("Enter a string:")))
    elif choice==8:
        print(fahrenheit_to_celsius(f=int(input("Enter temperature in Fahrenheit:"))))
    elif choice==9:
        print(celsius_to_fahrenheit(c=int(input("Enter temperature in Celsius:"))))
    elif choice==10:
        print(kg_to_pounds(kg=int(input("Enter weight in kilograms:"))))
    elif choice==11:
        print(pounds_to_kg(lb=float(input("Enter weight in pounds:"))))
    elif choice==12:
        print(is_palindrome(text=input("Enter a string:")))
    elif choice==13:
        print("exit")
except ValueError:
    print("please enter a valid number")
