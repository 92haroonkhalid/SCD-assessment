# arithmatic operations logic of addition, substraction, multiplication and division
def main_logic(choice):
    # Input for choice from user
    if choice == 1:
        a = int(input("Enter first number : "))
        b = int(input("Enter 2nd number : "))
        print(f"Addition of {a} & {b} is = {a+b}")
    elif choice == 2:
        a = int(input("Enter first number : "))
        b = int(input("Enter 2nd number : "))
        print(f"Substraction of {a} & {b} = {a-b}")
    elif choice == 3:
        a = int(input("Enter first number : "))
        b = int(input("Enter 2nd number : "))
        print(f"Multiplication of {a} & {b} = {a*b}")
    elif choice == 4:
        a = int(input("Enter first number : "))
        b = int(input("Enter 2nd number : "))
        print(f"Division of {a} & {b} = {a%b}")
    
# intigration of logic plus ui for user
def calculator():
    # Here first we have just given simple greetings
    print("Welcome! To our calculator program.")
    choice = 0 
    # loop to make it ask again and again like calculator works so we don't have to run code again and again
    while choice != 10:
        # choice for user to select operation and then enter number to perform operation
        choice = int(input("Enter 1 for addition, 2 for substraction, 3 for multiplication, 4 for division\n && 10 for Exit."))
        main_logic(choice)

# calling main function to run the code 
calculator()
