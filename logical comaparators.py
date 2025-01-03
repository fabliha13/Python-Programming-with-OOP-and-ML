##OR/AND


gender = input("What is your gender? ").lower()
age = int(input("What is your age? "))

student = True

# if gender == "f" and age >= 15:
#     print("You can enter the party")

# else:
#     print("You are not allowed")

if gender == "f" or age >= 15:
    print("You can enter the party")

else:
    print("You are not allowed")