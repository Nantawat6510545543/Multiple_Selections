weight = int(input("Enter your weight in kg: "))
height = int(input("Enter your height in cm: "))
BMI = weight / ((height/100) ** 2)
print(f"Your BMI is {BMI:.2f}.")

if BMI < 18.5:
    print("You are underweight.")
elif 18.5 <= BMI < 25:
    print("You are normal.")
elif 25 <= BMI < 30:
    print("You are overweight.")
else:
    print("You are obese.")
