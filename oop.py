class Person:
#constructor

   def __init__(self, name, dob, color, weight, height):
        self.name = name
        self.dob = dob
        self.color = color
        self.weight = weight
        self.height = height

   def display(self):
        print(f"Name is {self.name} and DOB is {self.dob} ")
   def get_bmi(self):
       result = self.weight  / self.height**2
       return round(result, 2)

#blueprint for creating Objects

p1 = Person("Meshack", 19, "blue", 20, 30)
p2 = Person("Smiley", 22, "red", 30, 40)
p1.display()
p2.display()
p1.get_bmi()
#print(p1.get_bmi())
print(f"{p1.name} bmi is {p1.get_bmi()}")
print(f"{p2.name} bmi is {p2.get_bmi()}")