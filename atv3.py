"""
1 string1 = input("Digite a primeira frase: ")
string2 = input("Digite a segunda frase: ")

tamanho1 = len(string1)
tamanho2 = len(string2)

print(f"Conteúdo 1: {string1} | Tamanho: {tamanho1}")
print(f"Conteúdo 2: {string2} | Tamanho: {tamanho2}")

if tamanho1 == tamanho2:
    print("As duas strings possuem o mesmo tamanho.")
else:
    print("As duas strings possuem tamanhos diferentes.")

if string1 == string2:
    print("O conteúdo das duas strings é igual.")
else:
    print("O conteúdo das duas strings é diferente.")
===========================================================================
2 nome = input("Digite o seu nome: ")

nomeinvertido = nome[::-1] .upper()

print (nomeinvertido)

===========================================================================
3 nome = input("Digite o seu nome: ")

nome = "\n".join(nome)

print(nome)
===========================================================================
4 nome = input("Digite o seu nome: ")

for i in range(1, len(nome) + 1):
    print(nome[0:i])
===========================================================================
5 nome = input("Digite o seu nome: ")

for i in range(len(nome), 0, -1):
    print(nome[0:i])
===========================================================================
6 data = input("Digite a data (dd/mm/aaaa): ")
dia, mes, ano = data.split('/')

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
mes_extenso = meses[int(mes) - 1]

print(f"A data é {dia} de {mes_extenso} de {ano}")
===========================================================================
7 frase = input("Digite uma frase: ").lower()

totalvogais = 0
totalespacos = 0

for letra in frase:
    if letra == " ":
        totalespacos = totalespacos + 1
    if letra in "aeiou":
        totalvogais = totalvogais + 1


print(f"O total de vogais dessa frase é: {totalvogais}")
print(f"O total de espaços dessa frase é: {totalespacos}")
===========================================================================
8 frase = input("Digite uma frase: ").upper().replace(" ","")

fraseinvertida = frase[::-1]

if frase == fraseinvertida:
    print(f"A frase ou palavra {frase} é um palindromo")
else:
    print(f"A frase ou palavra {frase} não é um palindromo")
===========================================================================
9 cpfbruto = (input("Digite o seu CPF: (xxx.xxx.xxx-xx): "))

cpflimpo = cpfbruto.replace(".","").replace("-","")

if cpflimpo.isdigit():
    parte = cpflimpo[0:9]
    verificador = cpflimpo[9:11]
    print("CPF Valido")
else:
    print("CPF Invalido!")
===========================================================================
10 unidades = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "setes", "oito", "nove"]
especiais = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]

num = int(input("Digite um número de 0 a 99: "))

if num < 10:
    print(unidades[num])
elif 10 <= num <= 19:
    print(especiais[num - 10]) # Ex: 15 - 10 = índice 5 da lista especial
else:
    d = num // 10
    u = num % 10
    if u == 0:
        print(dezenas[d])
    else:
        print(f" {dezenas[d]} e {unidades[u]}")
===========================================================================
11 import random

personagens = ["Will Smith", "Seu Madruga", "Michael Kyle", "Chris Rock", "Raven Baxter"]
selecao = random.choice (personagens)

mascara = []
for letra in selecao:
    if letra == " ":
        mascara.append(" ")
    else:
        mascara.append("_")

while "_" in mascara:
    print(" ".join(mascara))
    chute = input("Digite uma letra: ").upper()
    for i in range(len(selecao)):
        if selecao[i].upper() == chute:
            mascara[i] = selecao[i]
print(" ".join(mascara))
print("Parabéns! Você adivinhou o personagem!")
===========================================================================
12 numero = input("Digite o seu telefone: ").replace("-","")

tamanhonumero = len(numero)

novotelefone = "3" + numero

if tamanhonumero == 7:
    print(f"{novotelefone}")
elif tamanhonumero == 8:
    print(f"{numero}")
else:
    print("Telefone Incorreto")
===========================================================================
import random
frutas = ["Abacaxi", "Laranja", "Maça", "Banana"]

selecao = random.choice(frutas)

letras = list(selecao.upper())

random.shuffle(letras)

embaralhada = "".join(letras)

print(f"A palavra embaralhada é: {embaralhada}")

palpite = input("Qual é a fruta? ").upper()

if palpite == selecao.upper():
    print("Boa! Você acertou!")
else:
    print(f"Que pena, era {selecao.upper()}.")
==========================================================================="""    
tabela = {
    "A": "4", "B": "8", "C": "<", "D": "|)", "E": "3",
    "F": "|=", "G": "6", "H": "#", "I": "1", "J": ",|",
    "K": "|<", "L": "1", "M": "|\\/|", "N": "|\\|", "O": "0",
    "P": "|*", "Q": "(,)", "R": "|2", "S": "5", "T": "7",
    "U": "|_|", "V": "\\/", "W": "\\/\\/", "X": "><", "Y": "`/", "Z": "2"
}

texto = input("Digite o texto para converter: ").upper()
texto_leet = ""

for letra in texto:
    if letra in tabela:
        texto_leet += tabela[letra] 
    else:
        texto_leet += letra 

print(f"\nOriginal: {texto}")
print(f"Leet:     {texto_leet}")



        
    