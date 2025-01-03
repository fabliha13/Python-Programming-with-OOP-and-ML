#bus fare problem from Mirpur to Banani


passenger_type = input("Are you a student? Y/N:").lower()
fare = 50

if passenger_type == "y":
    age = int(input("What's your age?"))
    if age<=18:
        new_fare = fare/2
        print(f"Your fare is {new_fare}")
    else:
        new_fare = (fare/2) + 5
        print(f'Yor fare is {new_fare}')

else:
    print(f'Your fare is {fare}')
