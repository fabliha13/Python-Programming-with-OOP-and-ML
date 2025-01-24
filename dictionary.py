fruit_dict = {"apple": 5, "mango":7, "banana": 2}

# #printing items of a dict

# for k,v in fruit_dict.items():
#     print(k)

# # accessing the value
# no_of_banana= fruit_dict["banana"]
# print(no_of_banana)

# no_of_apple = fruit_dict.get("apple")
# print(no_of_apple)

# #removing a certain item from dict
# fruit_dict.pop("mango")
# print(fruit_dict)

# #adding a new item to the dictionary
# fruit_dict.update({"grapes" : 12})


# fruit_dict["papaya"] = 6
# print(fruit_dict)

# #removing the last item of the dictionary
# fruit_dict.popitem()
# print(fruit_dict)

numbers = {}

for num in range(0,6):
    numbers[num] = num**2

print(numbers)
