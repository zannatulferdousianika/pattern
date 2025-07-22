
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")


choice = input("Enter your choice 1/2: ")

if choice == '1':
    c = float(input("Enter temperature in Celsius: "))
    ctof = (c * 9/5)+32
    print("The convet from C to F is: ", ctof)
elif choice == '2':
    f = float(input("Enter temperature in Fahrenheit: "))
    ftoc = (f - 32) * 5/9
    print("The convet from F to C is: ", ftoc)
else:
    print("Invalid index..Put valid temparature")    
    

