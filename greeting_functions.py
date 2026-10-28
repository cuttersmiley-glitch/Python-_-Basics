from main import radius


def greet():
    print("Hello Hellen")

def greeting(name):
    print(f"Hello {name}")

def volume_cylinder(radius, height):
    v = 22/7 * radius**2 * height
    print(v,2)
def volume_cylinder_better(radius, height):
    v = 22/7 * radius**2 * height
    return v

def volume_surface(radius, height):
    v = 22/7 * radius**2 * height
    a = 22/7 * radius**2 * 2 + 22/7 * radius * 2 * height
    return v,a
#greeting("Mary")
#greeting("Akoth")
#greeting("kemboi")
#volume_cylinder(7, 20)
#volume_cylinder(14, 20)

#result = volume_cylinder_better(6.5, 8.9)
#print(round(result,3))

#with open("volumes.txt", "w") as file:
   # file.write(str(result))

volume, area = volume_surface(10,20)
print(f"volume is {volume} and area is {area}")

def divide(x, y, should_round):
    res =  x / y
    if should_round == True:
        return round(res,2)
    else:
        return res
print(divide(9,5.11, should_round=True))
