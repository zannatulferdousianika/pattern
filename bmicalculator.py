a = float(input("Enter your height (in m): "))
b = float(input("Enter your weight(in kg): "))

c = b / (a**2)

print("Your BMI is:",c)

if c < 16 :
    print("You have to eat more")
elif 16 > c <= 17:
    print("You are normal") 
elif c >= 25      

