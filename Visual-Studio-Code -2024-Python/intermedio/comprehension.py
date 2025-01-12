# Comprehension list

normal_list = [1,2,3,4,5,6,7]
print(normal_list)

def sum_number(number):
    number += "_"
    return number

my_string = "suscribite"
comprehension_list = [sum_number(i) for i in my_string]
print(comprehension_list)