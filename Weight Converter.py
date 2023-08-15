#Weight Converter
weight = float (input ("Weight: "))
unit = str (input ("(K)g or (L)bs: "))
if unit.upper() == "K":
    print ("Your weight in Lbs is:" + str(weight/0.45))
elif unit.upper() == "L":
    print ("Your weight in Lbs is:" + str (weight*0.45))