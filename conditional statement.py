## if, elif, else


#example 1

weather = input("What's the weather in your area today?Sunny/Rainy/Foggy? ").lower()


if weather == "sunny":
    print("Stay hydrated. Wear Sunscreen. Carry sunglass.")

elif weather == "rainy":
    print("Carry Raincoat and Umbrella.")

elif weather == "Foggy":
    print("Have a glass of warm coffee. Wear warm clothes.")

else:
    print("Invalid input")


