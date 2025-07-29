student2 = {
    "name" : "Zannatul Ferdous",
    "age"  : 16,
    "email" : "zannatul@gmail.com",
    "grade" : "A+",
    "job"  : "Coder",
    "is_active" : True
    
}


print("Orginal Dictionary :", student2)

print("Name:", student2["name"])

student2["courses"] = "Math , Chemistry"
print("After adding courses:",student2)

student2["grade"] = "A-"
print("After updating grade:", student2)

removed_age = student2.pop("age")
print("Removed age:",removed_age)
print("After removing age:", student2)

print("gender:",student2.get("gender","Not provided"))  
print("email:",student2.get("email","Not provided"))   

print("keys",list(student2.keys()))
