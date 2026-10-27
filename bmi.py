weight = input("Please enter your weight in Kgs:  ")
height = input("Please Enter your  height in m: ")

w = float(weight)
h = float(height)

bmi = w / h**2
if bmi < 18.5:
    print("You are under weight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("You are healthy")
elif bmi >= 25.0 and bmi <= 29.9:
    print("You are Overweight")
elif bmi >= 30 and bmi <= 34.9:
    print("You are obese class 1")
elif bmi >= 35 and bmi <= 39.9:
    print("You are obese class 2")
else:
    print("you are obese class 3")
