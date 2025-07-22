def operations():
    print("Select an operation: ")
    print("1. Addition ")
    print("2. Substraction ")
    print("3. Multiplication")
    print("4. Division ")

def take_input():
    choice = int(input("Enter choice (1/2/3/4): "))  
    if choice in (1,2,3,4):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return choice, num1, num2
    else:
        print("Invalid choice...")
        return take_input()

def calculate():
    choice,num1,num2 = take_input()  
    print("--------------------")
    if choice == 1:
        result = num1 + num2
        print(f"The result of {num1}+{num2} is: {result:0.2f} ") 
    elif choice == 2:
        result = num1 - num2
        print(f"The result of {num1}-{num2} is: {result:0.2f} ") 
    elif choice == 3:
        result = num1 + num2
        print(f"The result of {num1}*{num2} is: {result:0.2f} ")  
    elif choice == 4:
        if num2 != 0:
         result = num1 / num2
         print(f"The result of {num1}/{num2} is: {result:0.2f} ") 
        else: 
         print("Error!!Division by zero not allowed...") 

if __name__ == "__main__":
   print("------Calculator------")
   operations()
   print("----------------------")
   calculate()
   print("----------------------")
               
