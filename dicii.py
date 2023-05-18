my_dict = {
    "David" : 35,
    "Erika" : 32,
    "Jaime" : 50,
}

print(my_dict["David"])

my_dict["Pedro"] = 70

print(my_dict)

##del my_dict["Jaime"]

for valor in my_dict.values():
    print(valor)


for llave, valor in my_dict.items ():
    print(llave, valor)