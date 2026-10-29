def add(a, b, c):
    res =  a + b + c
    return res
def addition(x, y, *nums):
    total = sum(nums)
    return total

def build_profile(**kwargs):#dict key-word args
    for k, w in kwargs.items():
        print(f"{k}: {w}")

build_profile(experience= 100, name="Jane", age="21")

def mesh_function(name, *nums, **kwargs):
    print(name)
    print(nums)
    print(kwargs)
#Anonymous # lambda
#def square(num):
  #  return num ** 2

#result = square(5)
#print(result)
#square = lambda num: num ** 2
#print(square(5))
#res = square(2, 9)
#print(res)

surface_area_cylinder = lambda r, h: 22/7 * r**2 + 22/7 * 2 * r * h
print(surface_area_cylinder(14, 20))

people = [
    {"name": "Joy", "age": "21"},
    {"name": "Mary", "age": "22" },
    {"name": "Meshack", "age": "23"},
]
#lambda p:p['age']
sorted_by_age = sorted(people, key=lambda p: p["age"], reverse=True)
print(sorted_by_age)


#call function
#print(add(9,7,5))
#print(addition(6, 8, 5, 10))
#print(addition(6, 8, 10))