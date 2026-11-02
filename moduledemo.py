#means lib based work means module
# like import the user define  Lib

import UDF
while True:
    print("*" *50)
    print("1. OddEven Demo")
    print("2. maxofTwo Demo ")
    print("3. maxofThree Demo ")
    print("4. prime Demo")
    print("5. Febonacci Demo")
    print("6. Exit")
    print("*" *50)
    choice = int(input("Enter Your choice: "))

    if choice == 1:
        a= int(input("Enter value for A : "))
        print("*" *50)
        UDF.oddeven(a)
        print("*" *50)

    elif choice == 2:
        a= int(input("Enter value for A :"))
        b= int(input("Enter value for B :"))
        print("*" *50)
        UDF.maxoftwo(a,b)
        print("*" *50)

    elif choice == 3:
        a = int(input("Enter value for A :"))
        b = int(input("Enter value for B :"))
        c = int(input("Enter value for C :"))
        print("*" *50)
        UDF.maxofthree(a,b,c)
        print("*" *50)
    elif choice == 4:
        n = int(input("Enter value for A :"))
        print("*" *50)
        UDF.prime(n)
        print("*" *50)
    elif choice == 5:
        a = int(input("Enter value for A :"))
        print("*" *50)
        UDF.febonacci(a)
        print("*" *50)
    elif choice == 6:
        print("Thank You for your choice ")
        break
    else :
        print("Invalid choice try again")