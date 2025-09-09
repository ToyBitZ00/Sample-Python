first_name = input("Your First Name: ")
last_name = input("Your Last Name: ")

full_name = f"{first_name} {last_name}"

age = input("Your Age: ")
car = input("Your Car: ")

student = bool(input("Are you a student [true / false]: "))

if (student == "True"):
    school = input("What school are you from: ")
else:
    print("\n")
    print(full_name)
    print(age, "yrs old")
    print(car)

if (student == "True"):
    print("You are a student")
    print("You are studying in: ", school)
else:
    print("You are not a student")
