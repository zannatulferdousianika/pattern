student = {
    "name" : "Mehdi hasan",
    "age"  : 27,
    "email" : "mehdihasan@gmail.com",
    "grade" : "A+",
    "job"  : "Coder",
    "is_active" : True
    
}

print("Orginal Dictionary :", student)

print("Name:", student["name"])

student["courses"] = "Math , Chemistry"
print("After adding courses:",student)

student["grade"] = "A-"
print("After updating grade:", student)

removed_age = student.pop("age")
print("Removed age:",removed_age)
print("After removing age:", student)

print("gender:",student.get("gender","Not provided"))  
print("email:",student.get("email","Not provided"))   

print("keys",list(student.keys()))
