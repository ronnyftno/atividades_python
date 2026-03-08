"""1 numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
if numero1 > numero2:
    print("O maior número é o:", numero1)
else:
    print("O maior número é o:", numero2) 
=======================================================================================================================================
2 numero = int(input("Digite um número: "))
if numero > 0:
    print("Esse número é positivo")
elif numero < 0:
    print("Esse número é negativo")
else:
    print("O número é 0")
=======================================================================================================================================
3 sexo = input("Qual é seu sexo?: ").upper()
if sexo == "F":
    print("Sexo Feminino")
elif sexo == "M":
    print("Sexo Masculino")
else:
    print("Sexo Invalido")
=======================================================================================================================================  
4 letra = input("Digite uma letra: ")
if letra in "AEIOUaeiou":
    print("Essa letra é uma VOGAL")
else:
    print("Essa letra é uma CONSOANTE")

=======================================================================================================================================
5 nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
=======================================================================================================================================
6 numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

if (numero1 > numero2 and numero1 > numero3):
    print("O maior número é: ", numero1)
elif (numero2 > numero1 and numero2 > numero3):
    print("O maior número é: ", numero2)
else:
    print("O maior número é: ", numero3)
=======================================================================================================================================
7 numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

if (numero1 > numero2 and numero1 > numero3):
    maior = numero1
elif (numero2 > numero1 and numero2 > numero3):
    maior = numero2
else:
    maior = numero3
if (numero1 < numero2 and numero1 < numero3):
    menor = numero1
elif (numero2 < numero1 and numero2 < numero3):
    menor = numero2
else:
    menor = numero3
print(f"O maior número é: {maior} e o menor número é: {menor}")

=======================================================================================================================================
8 produto1 = float(input("Digite o primeiro preço: "))
produto2 = float(input("Digite o segundo preço: "))
produto3 = float(input("Digite o terceiro preço: "))

if (produto1 < produto2 and produto1 < produto3):
    produtocxb = produto1
elif (produto2 < produto1 and produto2 < produto3):
    produtocxb = produto2
else:
    produtocxb = produto3

print(f"Você deve comprar o produto que custa R${produtocxb:.2F} para conseguir uma melhor economia")
=======================================================================================================================================
9 numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

if (numero1 > numero2 and numero1 > numero3):
    maior = numero1
elif (numero2 > numero1 and numero2 > numero3):
    maior = numero2
else:
    maior = numero3
if (numero1 < numero2 and numero1 < numero3):
    menor = numero1
elif (numero2 < numero1 and numero2 < numero3):
    menor = numero2
else:
    menor = numero3

meio = numero1 + numero2 + numero3
meio = meio - maior - menor

print(F"O maior número é {maior}, o número do meio é {meio} e o menor número é {menor}")
=======================================================================================================================================
10 turno = input("Qual é seu turno?: ").upper()
if turno == "V":
    print("Boa Tarde!")
elif turno == "M":
    print("Bom Dia!")
elif turno == "N":
    print("Boa Noite!")
else:
    print("Valor Invalido")
=======================================================================================================================================
11 salario_atual = float(input("Digite o seu salário: "))
if salario_atual <= 280.00:
    percentual = 20
elif salario_atual > 280.00 and salario_atual <= 700.00:
    percentual = 15
elif salario_atual >=700.00 and salario_atual <= 1500.00:
    percentual = 10
else:
    percentual = 5
valor_aumento = salario_atual * (percentual / 100)
novo_salario = salario_atual + valor_aumento
print(f"Houve um reajuste no seu salário atual de R${salario_atual:.2f} de {percentual}%, totalizando o aumento de R${valor_aumento:.2f} e seu salário passa a ser R${novo_salario:.2f}")
=======================================================================================================================================
12 valor_hora = float(input("Digite o valor da sua hora trabalhada: "))
hora_trabalhada = float(input("Digite quantas horas foram trabalhadas: "))
salario_bruto = hora_trabalhada * valor_hora 

if salario_bruto <= 900.00:
    percentual = 0
elif salario_bruto <= 1500.00:
    percentual = 5
elif salario_bruto <= 2500.00:
    percentual = 10
else:
    percentual = 20

ir = salario_bruto * (percentual / 100)
inss = salario_bruto * 0.10
fgts = salario_bruto * 0.11
sindicato = salario_bruto * 0.03

total_descontos = ir + inss + sindicato

salario_liquido = salario_bruto - total_descontos

print(f"O seu salario bruto é de R${salario_bruto:.2f} porém, com os descontos de Imposto de Renda R${ir:.2f} Inss R${inss:.2f} e Sindicato R${sindicato:.2f} \n"
      f"o salario liquido fica R${salario_liquido:.2f}, lembrando que a empresa também realizou o deposito no FGTS no valor de R${fgts:.2f}")

print(f"\nSalário Bruto: ({valor_hora:.2f} * {hora_trabalhada:.2f}) : R$ {salario_bruto:.2f}\n"
      
      f"(-) IR ({percentual}%)                      : R$ {ir:.2f}\n"
      f"(-) INSS (10%)                              : R$ {inss:.2f}\n"
      f"(-) Sindicato (3%)                          : R$ {sindicato:.2f}\n"
      f"(-)Total de descontos                          : R$ {total_descontos:.2f}\n"
      f"(+)Salário Liquido                             : R$ {salario_liquido:.2f}\n"
      f"(+)FGTS (11%)                                  : R$ {fgts:.2f}\n")
=====================================================================================================================================
13 dia = int(input("Digite um número de 1 a 7 para saber o dia da semana: "))

if dia == 1:
    print("o dia é Domingo")
elif dia == 2:
    print("o dia é Segunda")
elif dia == 3:
    print("o dia é Terça")
elif dia == 4:
    print("o dia é Quarta")
elif dia == 5:
    print("o dia é Quinta")
elif dia == 6:
    print("o dia é Sexta")
elif dia == 7:
    print("o dia é Sabado")
else:
    print("Valor Invalido")
    
=======================================================================================================================================
14 nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if media >= 9.0 and media <= 10.0:
    conceito = "A"
elif media >= 7.5 and media < 9.0:
    conceito = "B"        
elif media >= 6.0 and media < 7.5:
    conceito = "C"   
elif media >= 4.0 and media < 6.0:
    conceito = "D"
else:
    conceito = "E"

if conceito in "ABC":
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

print(f"Notas: {nota1} e {nota2}")
print(f"Média: {media:.1f}")
print(f"Conceito: {conceito}")
print(f"Situação: {situacao}")
=======================================================================================================================================
15 lado1 = float(input("Digite o tamanho do primeiro lado: "))
lado2 = float(input("Digite o tamanho do segundo lado: "))
lado3 = float(input("Digite o tamanho do terceiro lado: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("Os lados formam um Triangulo!")

    if lado1 == lado2 == lado3:
        print("Esse Triangulo é Equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Esse Triangulo é Isósceles")
    else:
        print("Esse Triangulo é Escaleno")
else:
    print("Os lados não formam um Triangulo!")
=======================================================================================================================================
16 import math 

a = float(input("Digite o valor de a: "))

if a == 0:
    print("A equação não é de segundo grau. Programa encerrado.")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = (b ** 2) - (4 * a * c)

    if delta < 0:
        print(f"Delta = {delta}. A equação não possui raízes reais.")
    
    elif delta == 0:
        raiz = -b / (2 * a)
        print(f"O Delta é zero. A raiz única é: {raiz}")
    
    else:
        raiz_delta = delta ** 0.5
        x1 = (-b + raiz_delta) / (2 * a)
        x2 = (-b - raiz_delta) / (2 * a)
        
        print(f"O Delta é {delta}. As raízes são:")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
=======================================================================================================================================
17 ano = int(input("Digite o ano: "))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print("O ano é bissexto")    
        else:
            print("Esse ano não é bissexto") 
    else:
        print("O ano é bissexto")
else:
    print("Esse ano não é bissexto")        
=======================================================================================================================================
18  data = input("Digite a data (dd/mm/aaaa): ")
dia, mes, ano = data.split('/')

dia = int(dia)
mes = int(mes)
ano = int(ano)

valida = False

if 1 <= mes <= 12:
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        ultimo_dia = 31
    elif mes in [4, 6, 9, 11]:
        ultimo_dia = 30
    else:
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            ultimo_dia = 29
        else:
            ultimo_dia = 28
    
    if 1 <= dia <= ultimo_dia:
        valida = True

if valida:
    print(f"A data {dia:02d}/{mes:02d}/{ano} é VÁLIDA.")
else:
    print("Data INVÁLIDA.")
=======================================================================================================================================
19 numero = int(input("Digite um número inteiro menor que 1000: "))

if numero >= 1000:
    print("Número inválido. Deve ser menor que 1000.")
else:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    partes = []

    if centenas > 0:
        if centenas == 1:
            partes.append("1 centena")
        else:
            partes.append(f"{centenas} centenas")

    if dezenas > 0:
        if dezenas == 1:
            partes.append("1 dezena")
        else:
            partes.append(f"{dezenas} dezenas")

    if unidades > 0:
        if unidades == 1:
            partes.append("1 unidade")
        else:
            partes.append(f"{unidades} unidades")

    resultado = ""
    n_partes = len(partes)

    if n_partes == 3:
        resultado = f"{partes[0]}, {partes[1]} e {partes[2]}"
    elif n_partes == 2:
        resultado = f"{partes[0]} e {partes[1]}"
    elif n_partes == 1:
        resultado = partes[0]

    if resultado:
        print(f"{numero} = {resultado}")
    else:
        print("0 = 0 unidades")
=======================================================================================================================================
20 nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media == 10:
    print(f"Média {media:.1f}: Aprovado com Distinção!")
elif media >= 7:
    print(f"Média {media:.1f}: Aprovado")
else:
    print(f"Média {media:.1f}: Reprovado")
=======================================================================================================================================
21 saque = int(input("Digite o valor do saque (entre 10 e 600 reais): "))

if saque < 10 or saque > 600:
    print("Valor inválido! O saque deve ser entre 10 e 600 reais.")
else:
    valor_restante = saque

    notas100 = valor_restante // 100
    valor_restante = valor_restante % 100

    notas50 = valor_restante // 50
    valor_restante = valor_restante % 50

    notas10 = valor_restante // 10
    valor_restante = valor_restante % 10

    notas5 = valor_restante // 5
    valor_restante = valor_restante % 5

    notas1 = valor_restante

    print(f"Para sacar a quantia de {saque} reais, o programa fornece:")
    
    if notas100 > 0:
        print(f"{notas100} nota(s) de 100")
    if notas50 > 0:
        print(f"{notas50} nota(s) de 50")
    if notas10 > 0:
        print(f"{notas10} nota(s) de 10")
    if notas5 > 0:
        print(f"{notas5} nota(s) de 5")
    if notas1 > 0:
        print(f"{notas1} nota(s) de 1")
=======================================================================================================================================
22 numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é ÍMPAR.")
=======================================================================================================================================
23 numero = float(input("Digite um número: "))

if numero == round(numero):
    print(f"O número {numero} é INTEIRO.")
else:
    print(f"O número {numero} é DECIMAL.")
=======================================================================================================================================
24 num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("\nQual operação você deseja realizar?")
print("1 - Soma (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")
operacao = input("Escolha a opção (1/2/3/4): ")

if operacao == '1':
    resultado = num1 + num2
elif operacao == '2':
    resultado = num1 - num2
elif operacao == '3':
    resultado = num1 * num2
elif operacao == '4':
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: Divisão por zero!")
        resultado = None
else:
    print("Opção inválida.")
    resultado = None

if resultado is not None:
    print(f"\nResultado da operação: {resultado}")
    
    if resultado % 2 == 0:
        p_i = "Par"
    else:
        p_i = "Ímpar"

    if resultado >= 0:
        p_n = "Positivo"
    else:
        p_n = "Negativo"
        
    if resultado == round(resultado):
        i_d = "Inteiro"
    else:
        i_d = "Decimal"

    print(f"O número é: {p_i}, {p_n} e {i_d}.")
=======================================================================================================================================
25 print("Responda apenas 'sim' ou 'nao' para as perguntas abaixo:")

pontos = 0

p1 = input("1. Telefonou para a vítima? ").strip().lower()
p2 = input("2. Esteve no local do crime? ").strip().lower()
p3 = input("3. Mora perto da vítima? ").strip().lower()
p4 = input("4. Devia para a vítima? ").strip().lower()
p5 = input("5. Já trabalhou com a vítima? ").strip().lower()

if p1 == "sim": pontos += 1
if p2 == "sim": pontos += 1
if p3 == "sim": pontos += 1
if p4 == "sim": pontos += 1
if p5 == "sim": pontos += 1

print("Classificação do suspeito:")
if pontos == 2:
    print("Suspeita")
elif 3 <= pontos <= 4:
    print("Cúmplice")
elif pontos == 5:
    print("Assassino")
else:
    print("Inocente")
=======================================================================================================================================
26 litros = float(input("Digite a quantidade de litros: "))
tipo = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").upper()

preco_a = 1.90
preco_g = 2.50
total = 0

if tipo == 'A':
    if litros <= 20:
        total = litros * (preco_a * 0.97)
    else:
        total = litros * (preco_a * 0.95)
elif tipo == 'G':
    if litros <= 20:
        total = litros * (preco_g * 0.96)
    else:
        total = litros * (preco_g * 0.94)
else:
    print("Tipo de combustível inválido.")

if total > 0:
    print(f"Valor a pagar: R$ {total:.2f}")
=======================================================================================================================================
27 kg_morango = float(input("Quantidade de morangos (kg): "))
kg_maca = float(input("Quantidade de maçãs (kg): "))

if kg_morango <= 5:
    preco_morango = kg_morango * 2.50
else:
    preco_morango = kg_morango * 2.20

if kg_maca <= 5:
    preco_maca = kg_maca * 1.80
else:
    preco_maca = kg_maca * 1.50

preco_total = preco_morango + preco_maca
peso_total = kg_morango + kg_maca

if peso_total > 8 or preco_total > 25:
    preco_total = preco_total * 0.90

print(f"Valor a pagar: R$ {preco_total:.2f}")
======================================================================================================================================="""
tipo = int(input("Escolha o tipo de carne (1-File Duplo, 2-Alcatra, 3-Picanha): "))
quantidade = float(input("Quantidade de carne (Kg): "))
cartao = input("Compra no cartão Tabajara? (S/N): ").upper()

if tipo == 1:
    nome_carne = "File Duplo"
    if quantidade <= 5:
        preco_total = quantidade * 4.90
    else:
        preco_total = quantidade * 5.80
elif tipo == 2:
    nome_carne = "Alcatra"
    if quantidade <= 5:
        preco_total = quantidade * 5.90
    else:
        preco_total = quantidade * 6.80
elif tipo == 3:
    nome_carne = "Picanha"
    if quantidade <= 5:
        preco_total = quantidade * 6.90
    else:
        preco_total = quantidade * 7.80

desconto = 0
if cartao == 'S':
    tipo_pagamento = "Cartão Tabajara"
    desconto = preco_total * 0.05
else:
    tipo_pagamento = "Dinheiro/Outros"

valor_final = preco_total - desconto

print("\n--- CUPOM FISCAL ---")
print(f"Tipo de carne: {nome_carne}")
print(f"Quantidade: {quantidade:.2f} Kg")
print(f"Preço total: R$ {preco_total:.2f}")
print(f"Tipo de pagamento: {tipo_pagamento}")
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {valor_final:.2f}")