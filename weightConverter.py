weight = float(input("Enter your weight : "))
unit = input("Enter the unit Kilogram or Ponds (type K or L) : ")
flag = False

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
elif unit == "L":
    weight = weight / 2.205
    unit = "kgs"
else:
    print(f"{unit} is not a valid unit")
    flag = True

if not flag:
    print(f"Your weight is : {round(weight,1)} {unit}.")