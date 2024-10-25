definitions = {}

def add_definition(key, definition, definitions):
    definitions[key] = definition

def find_definition(key, definitions):
    if key in definitions:
        print(definitions[key])
    else:
        print("Definition not found!")

def delete_definition(key, definitions):
    if key in definitions:
        del definitions[key]
        print("Definition with key:", key, "deleted!")
    else:
        print("Definition not found!")

def show_definitions(definitions):
    print(definitions)

def exit_app():
    print("Good bye!")


 
while(True):
    print("1: Add definition")
    print("2: Find definition")
    print("3: Delete definition")
    print("4: Show definitions")
    print("5: Exit")
 
    choice = input("What would you like to do? ")
 
    if (choice == "1"):
        key = input("Type the key you want to add: ")
        definition = input("Type the definition: ")
        add_definition(key, definition, definitions)
    elif (choice == "2"):
        key = input("What are you looking for? ")
        find_definition(key, definitions)
    elif (choice == "3"):
        key = input("Which definition do you want to delete? Type the key: ")
        delete_definition(key, definitions)
    elif (choice == "4"):
        show_definitions(definitions)
    elif (choice == "5"):
        exit_app()
        break
    else:
        print("You've picked wrong option. Try again!")
