try:
    n = int(input("Enter the number of rows: "))
    for i in range(n+2):
        for j in range(i+3):
         print("*",end="")
         print()
except ValueError as e:
    print("Error:",e)
    
    
    
       