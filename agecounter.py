age = int(input("Enter the age: "))

try:
if age < 0:
    print("Age cannot be negative..")
elif age > 18:
    print("You are able to join")
else:
    print("Sorry, you are to young to play")   
except ValueError as age:
    print("Error:",age)   
