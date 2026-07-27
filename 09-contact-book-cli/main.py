import json


def get_contacts():
    """Get name, phone and email from the user"""
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    return name , phone , email


def add_contact(contacts, name, phone, email):
    """Add a contact to the contacts list"""
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)


def search_contact(contacts, name):
    """Search for a contact in the contacts list"""
    for contact in contacts:
        if contact["name"] == name:
            return contact
    return None


def print_contact(contact):
    """Print a contact"""
    print(f"Name: {contact['name']}")
    print(f"Phone: {contact['phone']}")
    print(f"Email: {contact['email']}")


def delete_contact(contacts, name):
    """Delete a contact from the contacts list"""
    contact = search_contact(contacts, name)
    if contact is None:
        print("Contact not found")
        return
    contacts.remove(contact)
    print("Contact deleted")


def update_contact(contacts, name):
    """Update a contact in the contacts list"""
    contact = search_contact(contacts, name)
    if contact is None:
        print("Contact not found")
        return
    new_name = input(f"Name [{contact['name']}]: ")
    new_phone = input(f"Phone [{contact['phone']}]: ")
    new_email = input(f"Email [{contact['email']}]: ")
    if new_name:
        contact["name"] = new_name
    if new_phone:
        contact["phone"] = new_phone
    if new_email:
        contact["email"] = new_email
    print("Contact updated")


def save_contacts(contacts, filename):
    """Save the contacts list to a file"""
    with open(filename, "w") as f:
        json.dump(contacts, f)
    print("Contacts saved")


def load_contacts(filename):
    """Load the contacts list from a file"""
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def main():
    """Main function of the program"""
    print("Welcome to the contact book")
    contacts = load_contacts("contacts.json")
    while True:
        print("1. Add contact")
        print("2. View contacts")
        print("3. Search contact")
        print("4. Delete contact")
        print("5. Update contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
        except ValueError:
            print("Invalid choice")
            continue
        if choice == 1:
            name, phone, email = get_contacts()
            add_contact(contacts, name, phone, email)
            save_contacts(contacts, "contacts.json")
        elif choice == 2:
            for contact in contacts:
                print_contact(contact)
        elif choice == 3:
            name = input("Enter name to search: ")
            contact = search_contact(contacts, name)
            if contact:
                print_contact(contact)
            else:
                print("Contact not found")
        elif choice == 4:
            name = input("Enter name to delete: ")
            delete_contact(contacts, name)
            save_contacts(contacts, "contacts.json")
        elif choice == 5:
            name = input("Enter name to update: ")
            update_contact(contacts, name)
            save_contacts(contacts, "contacts.json")
        elif choice == 6:
            break
        else:
            print("Invalid choice")
        print("-" * 50)


if __name__ == "__main__":
    main()