#AULA COMPLETA: NUMEROS EM PYTHON

"""
Vamos aprender:
1 - Tipos numéricos
2 - Conversões de tipos
3 - Hierarquia numérica
4 - Operações matemáticas
5 - Coerção de tipos
6 - Verificação de tipos
7 - Entrada de dados
"""
#===============================================================
## PASSO 01 - TIPOS NUMÉRICOS
#===============================================================
# INT -> números inteiros
# float -> números com casas decimais
# complex -> números complexos (usado em matemática/engenharia)

print ("===== TIPOS NUMÉRICOS =====")

# EXEMPLO 01 - NUMERO INTEIRO

#criamos uma variavel chamada numero_inteiro
numero_inteiro = 10

#Mostramos o valor
print ("Valor:", numero_inteiro)

#Type () mostra qual é o tipo da variável
print ("Tipo:", type(numero_inteiro))

print("---------------------------------")
#Exemplo 2 - NUMERO COM CASA DECIMAL

# criamos uma variavel chamada numero_decimal
numero_decimal = 3.14
# mostramos o valor
print("Valor:", numero_decimal)
# mostramos o tipo
print("Tipo:", type(numero_decimal))

print("---------------------------------")

# EXEMPLO 3 - NUMERO COMPLEXO
# criamos uma variavel chamada numero_completo
# Parte Real (2) + Parte Imaginaria (3j)

# estrutura geral:
# numero = a + bj

# a = parte real
# b = parte imaginária
# c = unidade imaginária
numero_complexo = 2 + 3j

# mostramos o valor
print("Valor:", numero_complexo)
# mostramos o tipo
print ("Tipo:", type(numero_complexo))

print("---------------------------------")

# EXEMPLO 3 - ACESSANDO CADA PARTE DO NÚMERO

# .real retorna a parte real
print ("Parte Real:", numero_complexo.real)

# .imag retorna a parte imaginária
print ("Parte Imaginária:", numero_complexo.imag)
# apenas para separar visualmente a saida no terminal
print("\n")

#================================================
## PASSO 02 - CONVERSÃO TIPOS
#================================================

## Exemplo Classico
## Dados vindos do usuario são texto (string), muitas vezes é necessário converter eles.

print("====== Conversões ======")

# float -> int

valor = int(3.9)

print("int(3.9):", valor)
print("Tipo:", type(valor))

#string ->int 
valor1 = "10"
print(type(valor1))

valor2 = int("10")
print('int("10"):',valor2)
print("tipo:", type (valor2))

#int --> float
valor3 = float(10)
print("float(10):", valor3)
print("tipo:", type (valor3))




      

