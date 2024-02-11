def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter both name and phone."
    return inner

contacts = {}

@input_error
def add_contact(args):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def get_phone(args):
    name = args[0]
    return contacts[name]

@input_error
def show_all_contacts(args):
    return '\n'.join([f"{name}: {phone}" for name, phone in contacts.items()])

while True:
    command = input("Enter a command: ").split()
    if command:
        action = command[0]
        args = command[1:]
        if action == "add":
            print(add_contact(args))
        elif action == "phone":
            print(get_phone(args))
        elif action == "all":
            print(show_all_contacts(args))
        else:
            print("Invalid command.")
