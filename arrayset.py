import array
ar = array.array('i',[25,30,35,70,50,89,68,70])

print("Array contents:",list(ar))

print("1.insert")
print("2.remove")
print("3.search")
print("4.exit")

choice = input("Enter your choice from (1-4): ")

if choice == '1':
    val = int(input("Enter the number you want to add: "))
    ar.append(val)
    print(f"{val} added")
    print("array contents: ", list(ar))



elif choice == '2':
    val = int(input("Enter the number you want to remove: "))
    if val in ar:
        print(ar.remove(val))
        print(f"{val} removed")
    else:
        print(f"{val} is not found") 

elif choice == '3':  
    val = int(input("Enter the number you want to search: "))      
    if val in ar:
        print(f"{val} found at index{ar.index(val)}")
    else:
        print(f"{val} is not found ")  

else:
    print("Invalid choice")





