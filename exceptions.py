def exceptions():


    try: 
        x = 1/0
    except ZeroDivisionError as e:
        print("Error: ",e)   

     
    try: 
        y = int("Anika")
    except ValueError as c:
        print("Error: ",c)    

    
    try: 
        data = ["25","10","12"]
        z = data[5]
    except IndexError as i:
        print("Error: ",i)   

     
    try: 
        d = {"a":1}
        key = d["b"]
    except KeyError as k:
        print(f"keyError: {k}") 

     
    try: 
        x = "mehdisir" + 100
    except TypeError as e:
        print(f"TypeError: {e} ")   

    
    try:
        with open("fyp.txt") as f:
           f.read()

    except FileNotFoundError as f:
        print(f"FileNotFoundError: {f} ")  

    
    try: 
        n = 5
        n.append(6)
    except AttributeError as n:
        print(f"AttributeError: {n}")     


     
    try: 
        print(result)
    except NameError as m:
        print(f"NameError: {m} ")   

    
    try: 
        10 == 12
    except:
        print("UnknownError")      

exceptions()                                 