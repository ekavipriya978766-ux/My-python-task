contacts = {}

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    contacts[name] = phone
    print("Contact Added Successfully!")

def search_contact():
    name = input("Enter Name to Search: ")
    if name in contacts:
        print("Phone Number:", contacts[name])
    else:
        print("Contact Not Found!")

def update_contact():
    name = input("Enter Name to Update: ")
    if name in contacts:
        phone = input("Enter New Phone Number: ")
        contacts[name] = phone
        print("Contact Updated Successfully!")
    else:
        print("Contact Not Found!")

def delete_contact():
    name = input("Enter Name to Delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact Deleted Successfully!")
    else:
        print("Contact Not Found!")

def display_contacts():
    if len(contacts) == 0:
        print("No Contacts Available!")
    else:
        print("\nAll Contacts:")
        for name, phone in contacts.items():
            print(name, ":", phone)

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        display_contacts()
    elif choice == "6":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")