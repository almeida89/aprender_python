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
print(convidados[6].title() + convite1)

print("\nFomos atualizados que podemos convidar somente duas pessoas.\n")

print(convidados[0], "sinto muito, mas você está fora.")
removido1 = convidados.pop(0)
print("\nAinda estão na lista: " + str(convidados) + "\n")

print(convidados[0], "sinto muito, mas você está fora.")
removido1 = convidados.pop(0)
print("\nAinda estão na lista: " + str(convidados) + "\n")

print(convidados[0], "sinto muito, mas você está fora.")
removido1 = convidados.pop(0)
print("\nAinda estão na lista: " + str(convidados) + "\n")

print(convidados[0], "sinto muito, mas você está fora.")
removido1 = convidados.pop(0)
print("\nAinda estão na lista: " + str(convidados) + "\n")

print(convidados[0], "sinto muito, mas você está fora.")
removido1 = convidados.pop(0)

print("\nOs únicos convidados que podem participar são: " + convidados[0] + " e " + convidados[1] + "\n")

print("O convidado " + convidados[0] + " comeu muito, e passou muito mal, foi embora, restou somente o " + convidados[1])
del convidados[0]

print("\nO " + convidados[0] + " bebeu demais, e foi preso! Acabou a festa")
del convidados[0]

print("\nFinalmente, todos foram embora, quer ver? A minha lista agora tem " + str(convidados))






