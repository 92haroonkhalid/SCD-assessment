print("Welcome! To our calculater.")
choice = 0
while choice != 5:
    choice = int(input("Enter 1 add, 2 sub, 3 mult, 4 div, 5 exit"))
    if choice == 1:
        a = int(input())
        b = int(input())
        print(a+b)
    elif choice == 2:
        a = int(input())
        b = int(input())
        print(a-b)
    elif choice == 3:
        a = int(input())
        b = int(input())
        print(a*b)
    elif choice == 4:
        a = int(input())
        b = int(input())
        print(a%b)