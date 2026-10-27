#if else
name = input("What is your name: ")
age = input("Enter your age:")
#if int(age) > 18:
    #print(name + "  You are old enough to vote")
#else:
  #  print(name + "  You are not old enough to vote")

if not age.isnumeric():
    print("Invalid age")
    #terminate

    if int(age) > 18:
        print(name + "  is an adult")
    else:
        print(name + "  is a child")