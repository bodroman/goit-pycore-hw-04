contacts = {}

def parse_input(user_input):
    parts = user_input.lower().split()
    command = parts[0]
    args = parts[1:]
    return command, args

def add_contact(name, phone):
    contacts[name] = phone
    print("Contact added.")

def change_contact(name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        print("Contact updated.")
    else:
        print("Contact not found.")

def show_phone(name):
    if name in contacts:
        print(contacts[name])
    else:
        print("Contact not found.")

def show_all():
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def main():
    while True:
        user_input = input("Enter command: ")
        command, args = parse_input(user_input)
        
        if command == "exit" or command == "close":
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) == 2:
                add_contact(*args)
            else:
                print("Invalid command.")
        elif command == "change":
            if len(args) == 2:
                change_contact(*args)
            else:
                print("Invalid command.")
        elif command == "phone":
            if len(args) == 1:
                show_phone(*args)
            else:
                print("Invalid command.")
        elif command == "all":
            show_all()
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
