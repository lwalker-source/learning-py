# logical operators = used on conditional statements

# and = checks two or more conditions if True
# or = checks if at least one condition is true
#not = true if condition is false, and vice versa


temp = 40
sunny = True

if temp <= 0 or temp >= 30:
    print("The temperature is bad.")
else:
    print("The temperature is good.")
    
if sunny:
    print("it is sunny outside")
else:
    print("It is cloudy outside")
