#This is a calculator

# This function adds two numbers
def add(x, y):
    return x + y
# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

def answer1():
    print (num1, "+", num2, "=", add(num1, num2))
def answer2():
    print((num1, "-", num2, "=", subtract(num1, num2)))
def answer3():
    print((num1, "*", num2, "=", multiply(num1, num2)))
def answer4():
    print((num1, "/", num2, "=", divide(num1, num2)))
def answer5():
    return exit()


def menu():
    print('#####################################')
    print('#                                   #')
    print('# Hello and Welcome to My Mini Calc!#')
    print('# Made By: Devon Porter             #')
    print('# Version 1.0                       #')
    print('#                                   #')
    print('#                                   #')
    print("# Please Select an operation        #")
    print('# 1. Addition                       #')
    print('# 2. Subtraction                    #')
    print('# 3. Multiplication                 #')
    print('# 4. Division                       #')
    print('# 5. Quite Program                  #')
    print('#                                   #')
    print('#                                   #')
    print('#####################################')
    

while True:
    # take input from the user
    menu()
    choice = input("Enter choice(1,2,3,4,5): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5'):
        if choice == '5':
            exit()
        num1 = float(input("Enter first number: "))
        if num1 == str():
            print("Invalid Input")

        num2 = float(input("Enter second number: "))
        if num2 == str():
            print("Invalid Input")

            
        if choice == '1':
            answer1()

        elif choice == '2':
            answer2()

        elif choice == '3':
            answer3()

        elif choice == '4':
            answer4()
        elif choice == '5':
            answer5

    else:
        print("Invalid Input")
print 
print(menu)
