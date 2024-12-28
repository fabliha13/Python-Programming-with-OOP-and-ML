my_string1 = "Abracadabra"

# print(my_string[-1])

length_of_my_string = len(my_string)
# print(length_of_my_string)

count_of_r = my_string.count("r")
# print(count_of_r)

day = "Sunday"

day2 = day.replace("Sun","Mon")
# print(day2)

fruit = "Mango is my favourite fruit."
idx_of_fav = fruit.find("favourite")
# print(idx_of_fav)

fruit = "Applepie"

# idx1 = fruit.find("p")
# print(idx1)
# idx2 = fruit.rfind("p")
# print(idx2)

print(fruit.upper())
print(fruit.lower())

fruit1 = "Mango is my favourite fruit.".split()
print(fruit1)

fruit2 = "Mango,is,my,favourite,fruit".split(".")
print(fruit2)