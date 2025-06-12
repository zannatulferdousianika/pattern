def operations():
    print("Select an opperation you want to calculate")
    print("1. circumference of circle")
    print("2. area of circle")

def take_input():
    choice = int(input("Enter choice (1/2): "))  
    if choice in (1,2):
        num1 = float(input("Enter the radius number: "))
        return choice, num1
    else:
        print("Invalid choice...")
        return take_input()


def calculate():
    choice,num1 = take_input()
    print("--------------------")

    if choice == 1:
        result = 3.1416 * num1**2   
        print(f"The circumference of {num1} is: {result: 0.2f}") 

    elif choice == 2:
        result = 2*3.1416*num1
        print(f"The area of {num1} is: {result: 0.2f}")
    else:
        print("operation not found")    
           


if __name__ == "__main__":
   print("---------Circle---------")
   operations()
   print("-------------------------")
   calculate()
   print("-------------------------")
                    
