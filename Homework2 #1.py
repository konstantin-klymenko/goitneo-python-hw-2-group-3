def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

#Howmework#2
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
    return inner

#Howmework#2
def key_error_handler(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
    return inner

# Вітання користувача
def hello():
    return "How can I help you?"

# Для додавання нового контакту
@input_error
#Howmework#2
def add_contact(contacts, name, phone):
    contacts[name] = phone
    return "Contact added."

# Для зміни номера телефону у вже існуючого контакту
#Howmework#2
@key_error_handler
@input_error
def change_contact(contacts, name, new_phone):
    contacts[name] = new_phone
    return "Contact updated."

# Для виведення номера телефону за ім'ям
#Howmework#2
@key_error_handler
def show_phone(contacts, name):
    return contacts[name]

def show_all(contacts):
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

# Головна функція, яка керує взаємодією з користувачем
def main():
    # Створюємо словник для збереження контактів
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        # Користувач вводить команду
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        # Перевіряємо, чи користувач не хоче завершити роботу бота
        if command in ["close", "exit"]:
            print("Goodbye!")
            break

        # Обробляємо команди
        if command == "hello":
            print(hello())

        elif command == "add":
            if len(args) == 2:
                name, phone = args
                print(add_contact(contacts, name, phone))
            else:
                print("Invalid command: Give me name and phone please.")

        elif command == "change":
            if len(args) == 2:
                name, new_phone = args
                print(change_contact(contacts, name, new_phone))
            else:
                print("Invalid command: Give me name and phone please.")

        elif command == "phone":
            if len(args) == 1:
                name = args[0]
                result = show_phone(contacts, name)
                if result == "Contact not found.":
                    print("Contact not found.")
                else:
                    print(result)
            else:
                print("Invalid command.")

        elif command == "all":
            result = show_all(contacts)
            if result:
                print(result)
            else:
                print("No contacts in the list.")

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
