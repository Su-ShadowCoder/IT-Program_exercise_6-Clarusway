# # Exercise 1
# user_list1 = []
#
# while True:
#     user_input = input("Enter a element to make the first list \n"
#                        "(or press Enter to finish the first list): ")
#     if user_input == "":
#         break
#     user_list1.append(user_input)
# user_list2 = []
# while True:
#     user_input2 = input("Enter a element to make the second list \n "
#                         "(or press Enter to finish the second list): ")
#     if user_input2 == "":
#         break
#     user_list2.append(user_input2)
#
# # # key
# # # user_list1 = [1, 2, 3, 4]
# # # value
# # # user_input2 = [7, 8, 9, 10]
# # # enjoin
#
# my_dict = dict(zip(user_list1, user_list2))
# print(my_dict)

# # Exercise 2
# my_dict = {
#     'a': 1,
#     'b': 2,
#     'c': 3
# }
#
# user_input = input("Enter a key you want to check"
#                    " if its in the dictionary or not: ")
# if user_input in my_dict:
#     print(f"{user_input} is in the dictionary!")
# else:
#     print(f"{user_input} is NOT in the dictionary!")

# # Exercise 3.1
#
# red_objects = {'apple', 'crab', 'rose', 'strawberry',
#                'tomato', 'cherry'}
# fruits = {'orange', 'apple', 'strawberry', 'grape', 'kiwi', 'mandarin',
#           'banana', 'cherry'}
# red_fruits = red_objects & fruits
# non_red_fruits = fruits - red_fruits
# print(f"Red fruits: {red_fruits}")
# print(f"Fruits that aren't red fruits: {non_red_fruits}")

# # Exercise 3.2
#
# orange_objects = {'basketball',
#                   'fanta', 'orange', 'autumn leaves', 'mandarin'}
# orange_fruits = orange_objects & fruits
# red_orange_fruits = orange_fruits.union(red_fruits)
#
# objects_set1 = red_objects - fruits
# objects_set2 = orange_objects - fruits
# ultra_instinct_set = objects_set1.union(objects_set2)
#
# print(f"Here are all the red and orange fruits: {red_orange_fruits}.")
#
# print(f"Here are all the objects: {ultra_instinct_set}.")

# # Exercise 3.3
#
# combined_sexy_set = red_objects.union(orange_objects).union(fruits)
# print(f"Here are all the things in a list: {list(combined_sexy_set)}")
#
# Exercise 4
# my_dict = {0: 19, 1: 33, 2: 18, 3: 30, 4: 26}
# my_dict = {}
#
# if my_dict == {}:
#     print("This dictionary is empty")
# else:
#     print("This dictionary is not empty")

# # Exercise 5
#
# my_dict = {0: 19, 1: 33, 2: 18, 3: 30, 4: 26}
# sorted_values = sorted(my_dict.values())
# sorted_values_dict = dict(zip(my_dict.keys(), sorted_values))
# print(f"The sorted dictionary is: {sorted_values_dict}")
