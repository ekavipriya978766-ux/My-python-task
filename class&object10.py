class movie:
    def __init__(self,id,name,price,tickets,):
        self.id=id
        self.name=name
        self.price=price
        self.tickets=tickets
    def calculate_bill(self):
        print("total price=",self.price*self.tickets)
        return self.price*self.ticket
    def display(self):
        print("\n------booking details------")
        print("id",self.id)
        print("name",self.name)
        print("price",self.price)
        print("tickets",self.tickets)
        print("calculate_bill",self.calculate_bill)
    def book_tickets():
        id=int(input("enter the id"))
        name=input("enter the name")
        price=float(input("enter the price"))
        tickets=int(input("enter the ticket"))
        calculate_bill=input("enter the calculate_bill")
        file=open("movie_booking.txt","a")
        file.write(f"id:{id}\nname:{name}\nprice:{price}\ntickets:{tickets}\ncalculate_bill:{calculate_bill}\n")
        print("\ntickets b0oking successfully")
        file.close()
        movie=movie(id,name,price,tickets)
        movie.display()
    def view_booking():
        try:
            file=open("movie_booking.txt","r")
            print("\n-----all booking records-----")
            for line in file:
                data=line.strip().split(",")
                print("id",data[0])
                print("name",data[1])
                print("price",data[2])
                print("tickets",data[3])
                print("calculate_bill",data[4])
        except FileNotFoundError:
            print("no booking records found!")
    while True:
        print("\n====movie ticket booking====")
        print("1.book ticket")
        print("2.view booking")
        print("3.exit")
        choice=input("enter your choice:")
        if choice == "1":
            book_tickets()
        elif choice == "2":
            view_booking()
        elif choice == "3":
            print("thank you")
            break
        else:
            print("invalid choice")







