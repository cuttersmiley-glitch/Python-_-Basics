ages  = [21, 83, 45, 23, 45, 33, 90, 34, 67]
names = ["Mesh", "Joy", "Kogei", "kemboi", "jeroo"]
#functions
ages.append(31)
#ages.clear()
#ages.sort()
#ages.reverse()
print(len(ages))
print(ages)

names.sort()
joy_count = names.count("joy")
print(joy_count)
#prnt(len(names))
print(names)
#print(sum(ages)/len(ages))


#retrieve element
#print(ages[4])
#print(names[-1:] )
#print(names[3:])


# SET
scores = { 88, 78, 88, 65, 77, 78}
print(scores)
scores.add(90)
scores.remove(88)

#TUPLE IMMUTABLE
weekdays = ("Mon", "Tue", "Wed", "Thu", "Fri")
print(weekdays[0])

#Dictionary
person = {"name":  "jason", "age": 21, "weight": 60, "height": 1.88}
print(person["name"])
print(person["age"])


people = [
{"name":  "jason", "age": 23, "weight": 60},
{"name":  "mesh", "age": 24, "weight": 60},
{"name":  "joy", "age": 19, "weight": 60}
]
print(people[0]["age"])