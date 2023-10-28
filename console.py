from display import UserInterface

class ConsoleInterface(UserInterface):
    def display_contacts(self, contacts):
        for account in contacts:
            if account['birthday']:
                birth = account['birthday'].strftime("%d/%m/%Y")
                result = "_" * 50 + "\n" + f"Name: {account['name']} \nPhones: {', '.join(account['phones'])} \nBirthday: {birth} \nEmail: {account['email']} \nStatus: {account['status']} \nNote: {account['note']}\n" + "_" * 50
                print(result)

    def display_commands(self):
        print("Available commands: \n"
              "add - Add a new contact\n"
              "search - Search for contacts\n"
              "edit - Edit a contact\n"
              "remove - Remove a contact\n"
              "save - Save the address book to a file\n"
              "load - Load the address book from a file\n"
              "congratulate - Display birthday congratulations\n"
              "view - View all contacts\n"
              "exit - Exit the program")

    def display_message(self, message):
        print(message)