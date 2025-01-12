#strings

mi_first_string = "mi string con comillas dobles"
mi_second_string = "mi string con comillas simples" #comillas simples deberia ser aqui xd

print(mi_first_string, mi_second_string)
print("esto es un texto de una variable" + mi_first_string + "" + mi_second_string)

print(f"esto es una texto de una variable {mi_second_string} dajhagjiudahd")


other_string = "holo"

a,b,c,d = other_string

print(a)
print(b)
print(c)
print(d)

print(f"{a}{b}{c}{d}")

print(mi_first_string.upper())
print(mi_first_string.capitalize())
print(mi_first_string.lower())
print(len(mi_first_string.upper()))
print(mi_first_string.find("r"))
print(mi_first_string.count("l"))
print(mi_first_string.upper().isupper())
print(mi_first_string.lower().isupper())
