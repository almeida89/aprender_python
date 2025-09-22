'''
Comece com seu programa anterior. 
Acrescente uma instrução `print` no final de seu programa, especificando o nome do convidado que não poderá comparecer.
Modifique sua lista, substituindo o nome do convidado que não poderá comparecer pelo nome da nova pessoa que está convidando.
Exiba um segundo conjunto de mensagens com o convite, uma para cada pessoa que continua presente em sua lista.
'''

convidados = ["Jimi Hendrix ", "Ozzy Osbourne", "Jim Morrison", "Kurt Cobain"]
convite1 = ", você está convidado para o nosso jantar do Rock!"

print("\n" + convidados[0].title() + convite1)
print(convidados[1].title() + convite1)
print(convidados[2].title() + convite1)
print(convidados[3].title() + convite1)

print("\nAtenção, o convidado," + convidados[1] + ", não irá comparecer, pois acabou de morrer!")

falecido = convidados.pop(1)
convidados.insert(1, "Fábio Almeida")

print("\nA nova lista de convidados é " + str(convidados) + " pois, " + falecido + " acabou de morrer!\n")

print(convidados[0].title() + convite1)
print(convidados[1].title() + convite1)
print(convidados[2].title() + convite1)
print(convidados[3].title() + convite1)

print("\nAtenção, encontramos uma mesa maior, vamos aumentar nossa lista de convidados!!!")

convidados.insert(0, "Pedro Lucas")
convidados.insert(2, "Dr. Pum")
convidados.append("Vô Miltão")

print("\nA nova lista de convidados é " + str(convidados).title())

print("\n" + convidados[0].title() + convite1)
print(convidados[1].title() + convite1)
print(convidados[2].title() + convite1)
print(convidados[3].title() + convite1)
print(convidados[4].title() + convite1)
print(convidados[5].title() + convite1)
print(convidados[6].title() + convite1 + "\n")