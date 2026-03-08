"""
1 print(“Hello World”)

2 numero = input ("Digite um número: ")
print ('O número informado foi', numero)

3 numero1 = int (input("Digite um número: "))
numero2 = int (input("Digite um número: "))
print('a soma é: ',numero1 + numero2) 

4 nota1 = float (input("Digite um nota: "))
nota2 = float (input("Digite um nota: "))
nota3 = float (input("Digite um nota: "))
nota4 = float (input("Digite um nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
print("A média das notas é:", media) 

5 valormetros = float(input('digite o valor em metros: '))
print(f"o valor em centimetros é: {valormetros * 100}")

6 import math
raio = float(input('Digite o raio do círculo:'))
area = math.pi * (raio** 2)
print(f"A área do círculo é: {area}")

7 lado = float(input('Digite o valor do lado do quadrado: '))
area = lado * lado
dobro = area * 2
print(f"A área do quadrado é: {area}")
print(f"O dobro desta área é: {dobro}")

8 valor_hora = float(input("Quanto você ganha por hora? "))
horas_trabalhadas = float(input("Número de horas trabalhadas no mês: "))
salario_total = valor_hora * horas_trabalhadas
print(f"Salário total: R$ {salario_total:.2f}")

9 farenheit = float(input("Digite a temperatura em Fahrenheit: "))
celsius = 5 * ((farenheit - 32) / 9)
print(f"A temperatura em Celsius é: {celsius:.1f}°C")

10 celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"A temperatura em Fahrenheit é: {fahrenheit:.1f}°F")

11 n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
n3 = float(input("Digite um número real: "))
item_a = (n1 * 2) * (n2 / 2)
item_b = (n1 * 3) + n3
item_c = n3 ** 3
print(f"Resultado A: {item_a}")
print(f"Resultado B: {item_b}")
print(f"Resultado C: {item_c:.2f}")

12 gb = float(input("Digite o valor em Gigabytes (GB): "))
mb = gb * 1024
print(f"{gb} GB equivale a {mb:.0f} MB")

13 gb = float(input("Digite o valor em Gigabytes (GB): "))
mb = gb * 1024
kb = mb * 1024
print(f"{gb} GB equivale a:")
print(f"{mb:.0f} Megabytes (MB)")
print(f"{kb:.0f} Kilobytes (KB)")

14 peso = float(input("Digite o peso que foi pescado:"))
excesso = max(0, peso - 50)
multa = excesso * 4
if peso > 50: print(f"A multa foi de: R$ {multa:.2f}")
else: print("Não houve multa")

15 salariobruto = float(input("digite o seu salário: "))
IR = salariobruto * 0.11
INSS = salariobruto * 0.08
SINDICATO = salariobruto * 0.05
salario_liquido = salariobruto - IR - INSS - SINDICATO
print(f"O salario bruto é: R$ {salariobruto:.2f}")
print(f"E o salario liquido é de: R$ {salario_liquido:.2f}")

16 import math
m2 = float(input("Digite quantos m2 serão pintados: "))
latas = math.ceil(m2 / 54)
preco = latas * 80
print("O total de latas a serem compradas serão:", latas)
print(f"E o valor dessas latas sera de: R$ {preco:.2f}")

17 import math
m2_original = float(input("Digite a área a ser pintada (m²): "))
litros_puros = m2_original / 6
folga = litros_puros * 0.10
litros_totais = litros_puros + folga

latas = math.ceil(litros_totais / 18)
preco_latas = latas * 80

galoes = math.ceil(litros_totais / 3.6)
preco_galoes = galoes * 25

print("          MEMÓRIA DE CÁLCULO (COM FOLGA)          ")
print(f"Área a ser pintada: {m2_original:.2f} m²")
print(f"Tinta base:         {litros_puros:.2f} litros")
print(f"Folga (10%):        {folga:.2f} litros")
print(f"TOTAL DE TINTA:     {litros_totais:.2f} litros")

if preco_latas < preco_galoes:
    diferenca = preco_galoes - preco_latas
    print(f"MELHOR OPÇÃO: COMPRAR APENAS LATAS")
    print(f"Quantidade: {latas} lata(s) de 18L")
    print(f"Custo nesta opção: R$ {preco_latas:.2f}")
    print(f"\nPOR QUE É MELHOR?")
    print(f"Comprando latas, você economiza R$ {diferenca:.2f}")
    print(f"em relação aos galões, que custariam R$ {preco_galoes:.2f}.")

elif preco_galoes < preco_latas:
    diferenca = preco_latas - preco_galoes
    print(f"MELHOR OPÇÃO: COMPRAR APENAS GALÕES")
    print(f"Quantidade: {galoes} galão(ões) de 3.6L")
    print(f"Custo nesta opção: R$ {preco_galoes:.2f}")
    print(f"\nPOR QUE É MELHOR?")
    print(f"Comprando galões, você economiza R$ {diferenca:.2f}")
    print(f"em relação às latas, que custariam R$ {preco_latas:.2f}.")

else:
    print("EMPATE TÉCNICO!")
    print(f"Ambas as opções custam R$ {preco_latas:.2f}")

18 arquivo = float(input("Digite o tamanho do seu arquivo: "))
velocidade = float(input("Qual a velocidade da sua internet?: "))
velocidadereal = velocidade / 8
tempo = arquivo/velocidadereal
minutos = int(tempo // 60) 
segundos = int(tempo % 60)
print(f"O tempo aproximado de Download será de: {minutos} minutos e \
      {segundos} segundos")"""
