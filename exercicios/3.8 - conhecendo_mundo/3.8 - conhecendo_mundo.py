lugares_para_visitar = ['Tóquio', 'Cairo', 'Atenas', 'Londre', 'Canada']
print("Minha lista original")
print(lugares_para_visitar)

'''Agora, vamos usar a função sorted() para exibir a lista em ordem alfabética, sem alterar a lista original.'''
print("\nAqui está a lista em ordem alfabética:")
print(sorted(lugares_para_visitar))

'''Para provar que a lista original não foi modificada, vamos exibi-la novamente'''
print("\nA lista original permanece inalterada:")
print(lugares_para_visitar)

'''Podemos também usar sorted() para exibir a lista em ordem alfabética inversa, 
passando o argumento reverse=True.'''
print("\nAqui está a lista em ordem alfabética inversa:")
print(sorted(lugares_para_visitar, reverse=True))

'''E, mais uma vez, a lista original continua intacta.'''
print("\n A lista original ainda está na sua ordem original:")
print(lugares_para_visitar)

'''Agora, vamos usar o método reverse() para inverter a ordem da lista permanentemente.'''
print("\n Invertendo a ordem da lista:")
lugares_para_visitar.reverse()
print(lugares_para_visitar)

'''Usando reverse() novamente, podemos reverter a lista de volta à sua ordem original.'''
print("\nRevertendo a lista para a ordem original.")
lugares_para_visitar.reverse()
print(lugares_para_visitar)

'''Se quisermos alterar permanentemente a lista para a ordem alfabética, usamos o método sort().'''
print("\nOrdenando a lista permanentemente em ordem alfabética:")
lugares_para_visitar.sort()
print(lugares_para_visitar)

'''Finalmente, podemos usar sort() com reverse=True para ordenar a lista permanentemente em ordem alfabética inversa.'''
print("\nOrdenando a lista permanentemente em ordem alfabética inversa:")
lugares_para_visitar.sort(reverse=True)
print(lugares_para_visitar)