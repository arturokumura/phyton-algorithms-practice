#Métodos
tupla = (6,1,5,2,-1,4,3,9)
print(tupla)
print("all()=",all(tupla))
print("sorted()=", sorted(tupla))
t_enum = enumerate(tupla)
print("Objeto enumerate()=", t_enum)
for i in t_enum:
    print(i)
print("len()=", len(tupla), "max()=", max(tupla), "min()=", min(tupla), "sum()=", sum(tupla))
