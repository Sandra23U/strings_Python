
# Detectar Palindromo
aux = str(input("Diga uma frase: ")).strip().upper()
palavras = aux.split()
frase = ''.join(palavras)
tamanho = len(frase)-1
inverso = ''

for i in range(tamanho, -1, -1):
    inverso += frase[i]

print("O inverso de {} é {}".format(frase, inverso))

if frase == inverso:
    print("Forma um palíndromo")
else:
    print("Não forma um palíndromo")
    