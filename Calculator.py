#Calculator
#Luke Jones

import math #This is so i can access all the trigonometric functions 

def degrees_to_radians(x): #This is to convert the users imput of degrees to radians so that the answer can be calculated
    return x*math.pi/180 

def radians_to_degrees(a): #This is to convert the calculated answer from radians to degrees so they get the answer in the units they are looking for 
    return (a/math.pi)*180

symbol = input("What sum would you like to do?") #Primary question

if symbol == "TRIGONOMETRY":
    answer = input("Cos, tan, sin, acos, asin or atan?") #Secondary question
    if answer == "COS": #If a user inputs the answer of cos the output will be as follows
        x = float(input("Angle?"))
        x_rad = degrees_to_radians(x)
        hyp = float(input("Hypotenuse?"))
        cosAnswer = hyp * math.cos(x_rad)
        print(cosAnswer)

    elif answer == "TAN": #If a user imputs the answer of tan the output will be as follows
        x = float(input("Angle?"))
        x_rad = degrees_to_radians(x)
        adj = float(input("Adjacent?"))
        tanAnswer = adj * math.tan(x_rad)
        print(tanAnswer)

    elif answer == "SIN": #If a user imputs the answer of sin the output will be as follows
        x = float(input("Angle?"))
        x_rad = degrees_to_radians(x)
        hyp = float(input("Hypotenuse?"))
        sinAnswer = hyp * math.sin(x_rad)
        print(sinAnswer)

    elif answer == "ACOS": #If a user inputs the answer of acos the output will be as follows
        adj = float(input("Adjacent?"))
        hyp = float(input("Hypotenuse?"))
        a = math.acos(adj/hyp)
        a_deg_acos = radians_to_degrees(a)
        print(a_deg_acos)

    elif answer == "ATAN": #If a user inputs the answer of atan the output will be as follows
        opp = float(input("Opposite?"))
        adj = float(input("Adjacent?"))
        a = math.atan(opp/adj)
        a_deg_atan = radians_to_degrees(a)
        print(a_deg_atan)

    elif answer == "ASIN": #If a user inputs the answer of asin the output will be as follows
        opp = float(input("Opposite?"))
        hyp = float(input("Hypotenuse?"))
        a = math.asin(opp/hyp)
        a_deg_asin = radians_to_degrees(a)
        print(a_deg_asin)

elif symbol == "RECTANGLE_AREA":
    firstside = 0.0
    secondside = 0.0
    rectangleAnswer = 0.0
    
    firstside = float(input("First side?"))
    secondside = float(input("Second side?"))
    rectangleAnswer = firstside * secondside
    print(rectangleAnswer)

elif symbol == "RECTANGLE_VOLUME":
    length = 0.0
    breadth = 0.0
    height = 0.0
    rectangleAnswer = 0.0
    
    length = float(input("Length?"))
    breadth = float(input("Breadth?"))
    height = float(input("Height?"))
    rectangletAnswer = length*breadth*height
    print(rectangleAnswer)

elif symbol == "ADD":
    totaltwo = 0.0
    firstnumber = 0.0
    secondnumber = 0.0
    total = 0.0
    cont = ""
    conttwo = 0.0
    finaltotal = 0.0

    firstnumber = float(input("First number?"))
    secondnumber = float(input("Second number?"))
    total = firstnumber+secondnumber

    cont = str(input("Would you like to add another number?"))
    while cont == "YES":
       conttwo = float(input("What is the additional number?"))
       totaltwo = totaltwo+conttwo
       cont = str(input("Would you like to add another number?"))

    finaltotal = total+totaltwo
    print(finaltotal)

elif symbol == "MULTIPLY":
    totaltwo = 1.0
    firstnumber = 0.0
    secondnumber = 0.0
    total = 0.0
    cont = ""
    conttwo = 0.0
    finaltotal = 0.0

    firstnumber = float(input("First number?"))
    secondnumber = float(input("Second number?"))
    total = firstnumber*secondnumber

    cont = str(input("Would you like to times it by another number?"))
    while cont == "YES":
       conttwo = float(input("What is the additional number?"))
       totaltwo = totaltwo*conttwo
       cont = str(input("Would you like to times it by another number?"))

    finaltotal = total*totaltwo
    print(finaltotal)
       
elif symbol == "SUBTRACT":
    totaltwo = 0.0
    firstnumber = 0.0
    secondnumber = 0.0
    total = 0.0
    cont = ""
    conttwo = 0.0
    finaltotal = 0.0

    firstnumber = float(input("First number?"))
    secondnumber = float(input("Second number?"))
    total = firstnumber-secondnumber

    cont = str(input("Would you like to subtract another number?"))
    while cont == "YES":
       conttwo = float(input("What is the additional number?"))
       totaltwo = totaltwo-conttwo
       cont = str(input("Would you like to subtract another number?"))

    finaltotal = total-totaltwo
    print(finaltotal)

elif symbol == "DIVIDE":
    totaltwo = 1.0
    firstnumber = 0.0
    secondnumber = 0.0
    total = 0.0
    cont = ""
    conttwo = 0.0
    finaltotal = 0.0

    firstnumber = float(input("First number?"))
    secondnumber = float(input("Second number?"))
    total = firstnumber/secondnumber

    cont = str(input("Would you like to divide it by another number?"))
    while cont == "YES":
       conttwo = float(input("What is the additional number?"))
       totaltwo = totaltwo/conttwo
       cont = str(input("Would you like to divide it by another number?"))

    finaltotal = total*totaltwo
    print(finaltotal)

elif symbol == "FRA":
    answer=str(input("What fractional calculation would you like to do?"))

    if answer == "FRACTION_PERCENTAGE":
        n=0
        d=0
        f=0.0
        x=0
        
        n = int(input("What is the numerator of the fraction?"))
        d = int(input("What is the denominator of the fraction?"))
        f = 100/d*n
        x = round(f)
        print(x,"%")

    elif answer == "FRACTION_DECIMAL":
        n=0
        d=0
        f=0.0
        x=0.0
        
        n = int(input("What is the numerator of the fraction?"))
        d = int(input("What is the denominator of the fraction?"))
        f = 100/d*n
        x = f/100
        print(x)

    elif answer == "DEC/FRA":
        x = 0.0
        x = float(input("What is the decimal?"))
        y = x.as_integer_ratio()
        print(y[0],"/",y[1])
        
                

elif symbol == "INDICES":
    numberTotal=1
    number = float(input("What is the number?"))
    x = int(input("To the power of what?"))
    for counter in range(x):
        numberTotal=numberTotal*number
       
    print(numberTotal)

elif symbol == "STL":
    answer = str(input("What type of straight line question?"))

    if answer == "GRADIENT":
        x1 = float(input("What is the x value of the first coordinate?"))
        y1 = float(input("What is the y value of the first coordinate?"))
        x2 = float(input("What is the x value of the second coordinate?"))
        y2 = float(input("What is the y value of the second coordinate?"))
        y3 = y2-y1
        x3 = x2-x1
        z = y3/x3
        print(z)

    if answer == "EQU/STL":
        x1 = float(input("What is the x value of the first coordinate?"))
        y1 = float(input("What is the y value of the first coordinate?"))
        x2 = float(input("What is the x value of the second coordinate?"))
        y2 = float(input("What is the y value of the second coordinate?"))
        y3 = y2-y1
        x3 = x2-x1
        z = y3/x3
        a = x1*z
        b = a+y1
        print("y =",z,"x +",b)
        
    
    
    


        
    
    


