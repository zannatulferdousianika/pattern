def convertor(num):
    roman_map = {
        1:"I" , 2: "II", 3: "III", 4:"IV", 5:"V", 
        10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 
        400:"CD", 500:"D", 900:"CM", 1000:"M"
    }

    roman = ""
    for value in sorted(roman_map.keys(),reverse=True):

        while num >= value:
            roman += roman_map[value]
            num -= value
        return roman 

n = input("Enter a integer number")

print("Roman number:", convertor(n))


