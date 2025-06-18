# Problem: Input weight (kg) and height (m), calculate BMI and print the category:

# Underweight: < 18.5

# Normal: 18.5–24.9

# Overweight: 25–29.9

# Obese: 30+

weight =int(input("enter the weight"))
height =int(input("enter the height"))
bmi =weight /(height**2)
print ("bmi",bmi)
if bmi<18.5:
    print("underweight")
elif bmi<20:
    print("normal")
elif bmi<30:
    print("overweight") 
else:
    print("obese")   