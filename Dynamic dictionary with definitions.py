"""
Program, which will allow user:
1) Add new definitions
2) Search for existing definitions
3) Remove definitions
"""

dictionary = {}

#Inifinite loop
while(True):

    #Menu
    print()
    print("Welcome in the dynamic dictionary!")
    print("What would you like to do?")
    print("1) Add new definition")
    print("2) Search for an existing definition")
    print("3) Remove existing definition")
    print("4) Exit")

    #Input
    choice = input("Pick a number: ")

    if (choice == "1"):
        key = input("Provide a key for definition: ")
        definition = input("Provide a definition: ")
        dictionary[key] = definition
        print("Dictionary updated!")
    elif (choice == "2"):
        key = input("Provide a key you are looking for: ")
        if (key in dictionary):
            print(dictionary[key])
        else:
            print(key, "not found!")
    elif (choice == "3"):
        key = input("Provide a key you want to delete: ")
        if (key in dictionary):
            del dictionary[key]
            print(key, "deleted successfully!")
        else:
            print(key, "not found!")
    elif (choice == "4"):
        break
    else:
        print("You selected an invalid value!")
