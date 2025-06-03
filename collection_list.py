# my_list=["apple","orange","kiwi"]
# my_list.append("banana")
# print(my_list)

# my_list=["apple","orange","kiwi"]
# my_list.insert(2,"banana")
# print(my_list)

# my_list=["apple","orange","kiwi","apple"]
# my_list.remove("apple")
# print(my_list)

# my_list=["apple","orange","kiwi","apple"]
# my_list.pop(2)
# print(my_list)

# my_tuple=("apple","orange","kiwi")
# my_list=list(my_tuple)
# my_list.append("banana")
# my_tuple=tuple(my_list)
# print(my_tuple[::-1])

# my_set={"apple","kiwi","apple","orange"}
# print(my_set)
# # my_set[1]="orange"
# my_set.add("banana")
# my_set.remove("apple")
# print(my_set)

student = {"name": "Alice","age": 20,"grade": "A"}
print(student["age"])
student["course"]="bca"
print(student)
del student["age"]
print(student)