# Criando uma lista de rios
rios = ['Nilo', 'Amazonas', 'Yangtzé', 'Mississippi', 'Danúbio' ]
print(f"\nLista original de rios: {rios}")

# Adicionando um item ao final da lista com append()
rios.append('Volga')
print(f"\nAdicionando 'Volga' com append(): {rios}")

# Inserindo um item em uma posição específica com insert()
rios.insert(0, 'Ganges')
print(f"\nAdicionando 'Ganges' na posição 0 com insert(): {rios}")

# Removendo um item com del
del rios[3]
print(f"\nRemovendo o item na posição 3 com del: {rios}")

# Removendo o último item da lista com pop()
rio_removido = rios.pop()
print(f"\nRemovendo o último item com pop(): {rios}")
print(f"\nO rio removido foi: {rio_removido}")

# Removendo um item pelo valor com remove()
rios.remove('Nilo')
print(f"\nRemovendo 'Nilo' com remove(): {rios}")

# Ordenando a lista temporariamente com sorted()
print(f"\nLista ordenada temporariamente com sorted(): {sorted(rios)}")
print(f"\nA lista original continua a mesma: {rios}")

# Invertendo a ordem da lista permanentemente com reverse()
rios.reverse()
print(f"\nInvertendo a ordem da lista com reverse(): {rios}")

# Ordenando a lista permentemente com sort()
rios.sort()
print(f"\nOrdenando a lista permanentemente com sort(): {rios}")

# Ordenando a lista em ordem inversa permanentemente com sort(reverse=True)
rios.sort(reverse=True)
print(f"\nOrdenando a lista em ordem inversa com sort(reverse=Item): {rios}")

# Otendo o tamanho da lista com len()
print(f"\nO tamanho final da lista é: {len(rios)}")

