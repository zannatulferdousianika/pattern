list1 = [25,50,30,12]
list2 = [25,25,80,56]

def multiply(list1,list2):
    c = list1*10 + list2*5
    return c 

result = map(multiply,list1,list2)  
print(list(result))  
