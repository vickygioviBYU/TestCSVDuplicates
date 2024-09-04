vEdades = [0, 1, 2, 3, 3, 2, 1, 0, 0, 1, 2, 3]

vEdades_unicos = []
duplicados = []

for count, i in enumerate(vEdades):
    if i not in vEdades_unicos:
        vEdades_unicos.append(count)
    else:
        # DUPLICADOS


        index = vEdades.index(i)


        if index != count:


            duplicados.append((index, count))

print(duplicados)