while True:
    print("---student data---")
    print("1,add_details")
    print("2,view_details")
    print("3,edit_details")
    print("4,exit")
    choice=int(input("enter the choice"))
    try:
        if choice==1:
            name=input("enter the name")
            roll_no=input("enter the roll_no")
            dept=input("enter the dept")
            marks=input("enter the marks")
            file=open("student data.txt","w")
            print(file.write(f"name:{name}\nroll_no:{roll_no}\ndept:{dept}\nmarks:{marks}\n"))
            file.close()
        elif choice==2:
            file=open("student data.txt","r")
            print(file.read)
            file.close()
        elif choice==3:
            name=input("enter the name")
            roll_no=input("enter the roll_no")
            dept=input("enter the dept")
            marks=input("enter the marks")
            file=open("student data.txt","a")
            print(file.write(f"name:{name}\nroll_no:{roll_no}\ndept:{dept}\nmarks:{marks}\n"))
            file.close()
        elif choice==4:
            print("exit")
            break
    except ValueError:
        print("invalid choice")