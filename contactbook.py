contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = [phone, email, address]
    print("Contact added.\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
    else:
        print("\n--- Contact List ---")
        for name, details in contacts.items():
            print("Name:", name)
            print("Phone:", details[0])
            print("Email:", details[1])
            print("Address:", details[2])
            print("---------------------")
        print()

def search_contact():
    search = input("Search by name or phone: ")
    found = False
    for name, details in contacts.items():
        if search == name or search == details[0]:
            print("\nContact Found:")
            print("Name:", name)
            print("Phone:", details[0])
            print("Email:", details[1])
            print("Address:", details[2], "\n")
            found = True
    if not found:
        print("Contact not found.\n")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        phone = input("New phone: ")
        email = input("New email: ")
        address = input("New address: ")
        contacts[name] = [phone, email, address]
        print("Contact updated.\n")
    else:
        print("Contact not found.\n")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.\n")
    else:
        print("Contact not found.\n")

def menu():
    while True:
        print("=== Contact Manager ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")

# Run the menu
menu()
