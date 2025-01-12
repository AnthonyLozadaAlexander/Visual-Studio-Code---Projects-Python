# DICCIONARIOS

my_dict = {"a", "b"}

print(type(my_dict))

my_dict = {5:"Nicolas",
           "Apellido":"Gonzlez",
           "Apodo":"Nikorasu"}

print(type(my_dict))

print(my_dict[5])

print(my_dict.keys())
print(my_dict.values())

my_dict = list(my_dict)
print(my_dict)

my_dict = set(my_dict)
print(my_dict)

my_dict = tuple(my_dict)
print(my_dict)