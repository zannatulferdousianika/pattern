fruits = [ "mango","apple","banana","guava" ]
prices = [ 120,300,30,50 ]

data = {fruits : prices for fruits,prices in zip(fruits,prices)}
print(data)

