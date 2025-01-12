# SETS

my_set = {}
print(type(my_set))

my_set = {"python", "JavaScript", "C++"}
print(type(my_set))

# print(my_set[0]) TypeError: "set" objects is not subscriptable

my_set.add("C++")
print(my_set)
my_set.add("C#")
print(my_set)

my_set_0 = {"Python", "JavaScript", "C++"}
            
my_set.difference_update(my_set_0)
print(my_set)