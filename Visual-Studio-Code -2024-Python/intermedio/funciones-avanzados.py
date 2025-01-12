# funciones de orden superior

def add_value(num):
    return num + 5

def add_value_2(num):
    return num + 10

def sum_values(num1, num2, f):
    return f(num1 + num2)


print(sum_values(7, 8,add_value))
print(sum_values(7, 8,add_value_2))

# CLOSURES

def closure_number(original_num):
    def closure_new(num):
        return num ** original_num
    return closure_new

my_function = closure_number(3)
print(my_function(2))
print(my_function(5))

my_function_1 = closure_number(4)
print(my_function_1(2))

list_numbers = [7, 10, 15, 25]

def division_number(number):
    return number / 2

request = list(map(division_number, list_numbers))
request = list(map(lambda number: number * 2 , list_numbers))

# print(request)

def filter_number(number):
    return number > 10

request = list(filter(filter_number, list_numbers))
request = list(filter(lambda number: number > 15, list_numbers))

print(request)