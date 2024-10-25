#Hello app
print("Welcome in the Calculator 2024!")

#Show menu
menu = input("Choose an option: +, -, *, /, ** ")
print("Your choice is:", menu)

#A and B values
a = int(input("A = "))
b = int(input("B = "))

#Main section
if(menu == "+"):
    print("Result: ", a + b)
elif(menu == "-"):
    print("Result: ", a - b)
elif(menu == "*"):
    print("Result: ", a * b)
elif(menu == "/"):
    if(b == 0):
        print("Don't divide by zero!")
    else:
        print("Result: ", a / b)
elif(menu == "**"):
    print("Result: ", a ** b)
else:
    print("Choose proper option!")
