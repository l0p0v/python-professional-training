# -*- coding: utf-8 -*-
"""6_Funções_Builtin.ipynb



Prof. Fernando Amaral

www.eia.ai

# Funções Built IN
"""

num1 = -10
num2 = 10
print(abs(num1))
print(abs(num2))
print(abs(num1) + abs(num2))

maior_valor = max(10, 20, 30)
print(maior_valor)

lista = [-20, 1, 2.3, 3]
print(max(lista))

lista = [-20, 1, 2.3, 3]
print(min(lista))

x = 2
y = 3
print(pow(x, y))

import math

print(math.sqrt(25))

print(round(2.4566, 3))

from math import floor, ceil

print(floor(2.4566))
print(ceil(2.4566))

print(divmod(10, 4))

numero = 70
caractere = chr(numero)
print("O número %d é mapeado para o caractere %s " % (numero, caractere))

for i in range(70, 100):
    caractere = chr(i)
    print("%d - %s " % (i, caractere), end='\n')

caractere = "a"
numero = ord(caractere)
print("O caractere %s se mapeia para o número %d " % (caractere, numero))

texto = "olá, tudo bem?"
print(texto.capitalize())

texto = "IsTo é EstraNHO"
print(texto.lower())
print(texto.upper())
print(texto.swapcase())

texto = "eu sou um ótimo programador python"
print(texto.title())

texto = "1234567"
print(texto.center(9))
print(texto.center(14))
print(texto.center(14, '-'))

texto = "1234567"
print(texto.rjust(9))
print(texto.ljust(9))

texto = "12121212"
print(texto.count("121"))

texto = "12121212"
print(texto.startswith("12"))
print(texto.endswith("12"))

texto = "me encontra 20 10 5"
pos = texto.find("10")
print(pos)
pos = texto.find("4")
print(pos)

texto = "me encontra 20 10 5"
pos = texto.index("10")
print(pos)
# gera erro
# pos = texto.index("4")
# print(pos)

texto = "Ol@ eu sou @ ful@n@"
novo_texto = texto.replace("@", "a")
print(novo_texto)

texto = '10,20,30'
print(texto.split(","))

texto = "Olá, bom dia\n este é um curso de python\n seja bem vindo"
print(texto.splitlines())

print("abcdE3 ".isalpha())

print("abcdE3".isalnum())
print("abc,dE3".isalnum())

print("123.4".isdecimal())
print("123".isdecimal())
print("123a".isdecimal())

print("123".isspace())
print("1   ".isspace())
print("   ".isspace())

print("abc".islower())
print("ABC".isupper())

lista = [5, 10, 2, 1, 5, 10]
lista.sort()
print(lista)

lista = ["a", "b", "x", "ab", "d", "c"]
lista.sort()
print(lista)

lista = [5, 10, 2, 1, 5, 10]
lista.sort(reverse=True)
print(lista)


def sort_por_tamanho(item):
    return len(item)


lista = ["b", "ab", "de", "abcd", "abc", "a"]

lista.sort(key=sort_por_tamanho)
print(lista)

lista = [5, 10, 2, 1, 5, 10]
lista.reverse()
print(lista)

produtos = [['carro', 'R$ 100.000'],
            ['cadeira', 'R$ 1000'],
            ['Moto', "R$ 40000"],
            ['geladeira', 'R$ 20000'],
            ['armário', 'R$ 1500']]

for produto, valor in produtos:
    print(produto, valor)

nomes = ('José', 'Carlos', 'João')
dicionario = dict.fromkeys(nomes, 10)
print(dicionario)

import datetime

data_completa = datetime.datetime.now()

data = data_completa.date()
hora = data_completa.time()

print(data_completa)
print(data)
print(hora)

import datetime

data_completa = datetime.datetime.now()
print("Dia ", data_completa.day)
print("Mês ", data_completa.month)
print("Ano ", data_completa.year)
print("Hora ", data_completa.hour)
print("Minuto ", data_completa.minute)
print("Segundo", data_completa.second)

import datetime

data = datetime.date(2000, 9, 30)
data = datetime.date(day=30, month=9, year=2000)
print(data)
print(type(data))

import datetime

hora = datetime.time(10, 30, 20)
print(hora)

import datetime

data = datetime.datetime(2000, 9, 30, 10, 30, 20)
print(data)

import datetime

# y ano
# m mês
# d dia
# H hora
# M minuto
# S segundo
atual = datetime.datetime.now()
current_time = atual.strftime("%y/%m/%d %H:%M:%S")
print(current_time)
print(type(current_time))

import datetime

# y ano
# m mês
# d dia
# H hora formato 00-23
# M minuto
# S segundo

# A dia da semana
# a dia da semana abrev.
# B nome do mês
# b nome do mês abrev.
# I hora formato 12 horas
# p AM PM

data = datetime.datetime(2000, 9, 30, 10, 30, 20)
print(data.strftime("%A  - %a"))
print(data.strftime("%B  - %b"))
print(data.strftime("%H  - %I"))
print(data.strftime("%I  - %p"))

import datetime

data1 = datetime.datetime(2020, 10, 20)
data2 = datetime.datetime(2020, 11, 20)
diferenca = data2 - data1
print(diferenca)
print(type(diferenca))

from datetime import datetime, timedelta

data_atual = datetime.now()
datafutura1 = data_atual + timedelta(weeks=4)
datafutura2 = data_atual + timedelta(days=30)
datafutura3 = data_atual + timedelta(hours=12)
datafutura4 = data_atual + timedelta(minutes=60)

print("Data atual: ", data_atual)
print("Mais 4 semanas: ", datafutura1)
print("Mais 30 dias: ", datafutura2)
print("Mais 12 horas: ", datafutura3)
print("Mais 60 minutos: ", datafutura4)

import datetime

data_2000 = datetime.datetime(2000, 1, 1, 0, 0, 0)
data_agora = datetime.datetime.now()
diferenca = data_agora - data_2000

print("Desde o ano 2000 passou ", diferenca.days, " dias")
print("Desde o ano 2000 passou ", diferenca.seconds, " segundos")
print("Desde o ano 2000 passou ", diferenca.microseconds, " microsegundos")

anos = int(diferenca.days / 365)
meses = anos * 12

print("Desde o ano 2000 passou ", anos, " anos")
print("Desde o ano 2000 passou ", meses, " meses")

print(diferenca)

import datetime

data_txt = input("Digite a data no fomato dia/mês/ano:")
datetime = datetime.datetime.strptime(data_txt, "%d/%m/%Y")
print(datetime)
print(type(datetime))


# 1 - Crie uma função que retorne a subtração de dois elementos, mas que
# considere o valor absoluto deste valores.

def subtrai(num1, num2):
    return (abs(num1) - abs(num2))


print(subtrai(-200, 100))


# 2 – Sem usar “ifs”, crie uma função que receba dois números e retorne a soma
# dos mesmos, mas o valor retornado não pode passar de 10000 e deve ser 
# sempre maior que 0.

def soma(num1, num2):
    soma = num1 + num2
    soma = min(10000, soma)
    soma = max(0, soma)
    return soma


print(soma(20, 20))
print(soma(5000, 6000))
print(soma(10, -20))


# 3 (DESAFIO) - Crie uma função que receba argumentos de tamanho arbitrário.
# Todos esses argumentos serão números. Em seguida retorne o menor número 
# entre todos os recebidos.

def menor(*numeros):
    menor = numeros[0]
    for i in numeros:
        menor = min(i, menor)
    return menor


print(menor(10, 20, 30, 10000, -2))
print(menor(1000, -20, 10000, -2))

# 4 - Crie uma função que calcule a formula de Bhaskara, encontrado o X. 
# Os coeficientes a,b e c devem ser lidos por input.

import math

a = float(input("Digite o coeficiente a:"))
b = float(input("Digite o coeficiente b:"))
c = float(input("Digite o coeficiente c:"))

x1 = (-b + math.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)
x2 = (-b - math.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)
print("A solução encontrada é ", x1, x2)

"""![image.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAfIAAAB/CAYAAAAUyEBiAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAFxEAABcRAcom8z8AAEHJSURBVHhe7d0LvG9TtQfwbkmI6ibETZIued0SrhQVIq/keVNXFElyvV/JI/IIhTy7KM/yCuUtjxQSlVe5IiSPIqGS8jjnWHd/59ljW2ed/3/v/3/v/95nn3PG75zxWf/9/6/HXGvNOX9jjDnmmK+oEolEIpFITLdIIk8kEolEYjpGEnkikegpXnrppSKJRGJskESeSCR6BgQ+adKkqYg8iT2RGD0kkScSiZ6hSeS2EydOLN8lEoneQ9tKIk8kEqOKtMYTidFFEnkikegpwiqvW+E+s8y7lThPq9/Gq0yYMCElZUwk6lsSeSKR6BmQuI7l+eefLwT8wgsvVL/5zW+q66+/vrrqqquGLT/84Q8H5MorrxzXcsUVV6SkjImob9pEEnkikegpwoJG6r/97W+rvffeu9p4442r9dZbr/rYxz7WlTimlXz0ox9NSUnpE+0hiTyRSIwKnnrqqerEE0+sll9++WrZZZet1l133WrDDTes1l9//RHJBhts0LXEsa4f4vvmVqdIgahfLyVlvErU1STyRCIxKvjpT39aiPGd73xntf3221ff//73ixvw8ssvH5E0Xdl1qbvg6xK/N930/q5/f8kll1SXXnppSzdmSsp4FPU3iTyRSPQUXOp/+9vfquOPP756xzveUX3kIx+pzjvvvOovf/lLGTN/9tlnO5J//vOfLeW5555rKc+/8Hw5/4svvjiV+L789sKLZfyeRKCQY8vvz79QPffPvvP0/dbqHCkp41WSyBOJDoCcSGJo6FhuvvnmapNNNqkWXHDB6rDDDqvuv//+/l8TiUSvkUSemCaY3kgxibwzeEZ/+tOfqqOOOqp6+9vfXsbGr7766mJJjwVcP4LtbANPPvlkdd1111UnnXRSUSwOP/zwMn7Pnf7www8X5SORmF6RRJ6YJpieSLGQw0tTZitLtAa39C9+8YvqU5/6VPXWt7612m233cr0My5sz220n53zh8vclgLxq1/9qrj5P/7xj1f/8R//Ub3lLW+p5ptvvuptb3tbtcYaa1Rf+cpXqmuvvbb60+N/6j/LZER5KQSjXe4ZCn2ParDnFc81n2nvkESeGBVopDr1Z555pvrrX/9aRKca05Kmp0asrDrzSRMnd+hFJumt+neYidEkuccff7w644wzqpVWWqlabbXVqh//+Mclet0YNHINK1ndUCeefvrpMp5unLpuQQ8XA++qT/7+978XpeJ//ud/qhVWWKFEz6+yyiplzH7FFVesFllkkWqBBRao/v3f/7365Cc/WZ199tml/HE/tsrMWrdNdAbPPtq5z/X6AfF+mt8nho8k8kRPEY1T52cOsQjgs846qzr//POrX/7yl8XFqRFPTygdUh+JT3hxspVXvusj8pm9I/Ie6+Rse/vtt1c77bRT9Z73vKfaY489ipsdSasPdSVO3bjssstKvVBH7rnnnrJPdPDDfbZxnHLddddd1V577VWi5hG38lAyLrroour000+v9t133zIlbv755y+EbkxfeSgY4FzeeZEk8o7hHYbSWz73149AvN94V4mRI4k80VOEpcoa0imydFhB5jsec8wxA27W6Q1ISLmDyBMvE3m8T5HmP/jBD6o111yzWOPe/z/+8Y/yexA02F588cXVlltuWa211lrVf//3f1fnnntu2dfzre87XCBj53zXu95VLb300tXBBx9c3XnnnaVe8g74XQCeKXGS1XC1I3RluePOO8o51OVCSP1KWxJPZyh9QGJMkUSe6CnC6jLV6Otf/3oZj3zFK15R/eu//mtxcYpm5lad3hAdueEBwVGsvccee2ymJ3bPJIgcMSJM1q954/5u93z+93//t1jK//Iv/1II9NBDDy0kG8+ZDBeuibRZ4OofD8Edd9xRPAPxe5TL+/z2t79dffCDH6xmn3324m7nKYCwKhPdw5DaHbffUd12223FS+P533fffUXZS/QeSeSJnkIHqfMLIjf9CJG/9rWvrbbddtvqlltuma4jhB966KHquOOOq9Zee+3qpBNPqp79e3ZM3jcrmgUueOx973tfdcoppwy41Fu5Vo899thCmurGm9/85hJJjlTjXCMhUOeR2EWmtiWWWKIkkYnz2TY9K8hG3ZxnnnlKfb3gggsmlyOJfFjwbHlcDK94x4suumiJUdhhhx3KEErAs83n2xskkSd6iui0uS7rRD7nnHNW22yzTfWzn/1swIIbT4hOpZ0EWJn77LNP9W//9m/VnnvsWT3+2OP9v0w+x8wE7zrk3nvvrXbffffq3e9+d4lY954hFLs6/I3I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)"""


# 5 - Crie uma função que receba uma string, e para cada letra minúscula a
# transforme em uma letra maiúscula e vice versa.

def troca(texto):
    return texto.swapcase()


print(troca("Olá MunDO"))


# 6 - Crie uma função receba uma string e uma letra do alfabeto.
# Retorne a quantidade de vezes que essa letra tem na string. 
# Caso não ocorra nenhuma vez, retorne 0.

def conta(texto, caracter):
    return texto.count(caracter)


print(conta("abcaa", "a"))
print(conta("abcaa", "d"))


# 7 (DESAFIO) - Crie uma função receba uma string e uma letra do alfabeto.
# Retorne uma lista contendo o índice de onde todas as ocorrências aparecem.

def encontra_ocorrencias(texto, caracter):
    indices = []
    indice = 0
    for char in texto:
        if (char == caracter):
            indices.append(indice)
        indice += 1
    return indices


print(encontra_ocorrencias("abcaa", "a"))
print(encontra_ocorrencias("abcab", "b"))


# 8 - Crie uma função que receba o que foi digitado pelo usuário no chat e
# também uma lista contendo todas as palavras não permitidas a serem digitadas. 
# Essa função então retornara o que foi digitado pelo usuário mas no lugar 
# das palavras não permitidas retorna o caractere '*’.

def retira_palavras(texto, palavras):
    for palavra in palavras:
        if palavra in texto:
            texto = texto.replace(palavra, "*")
    return texto


texto_usuario = "não pode falar a palavra droga ou diabo no chat"
palavras_proibidas = ['droga', 'diabo']
print(retira_palavras(texto_usuario, palavras_proibidas))


# 9 - Crie uma função que retorne verdadeiro se uma string é totalmente
# maiúscula ou totalmente minúscula.

def e_maiscula_ou_minuscula(texto):
    return texto.islower() or texto.isupper()


print(e_maiscula_ou_minuscula("AAAAAAA"))
print(e_maiscula_ou_minuscula("AAAdafad"))
print(e_maiscula_ou_minuscula("fafadfa"))


# 10 - Crie uma função que receba uma lista de textos.
# Detecte quais os valores dessa lista são inteiros e em seguida transforme 
# eles para um número do tipo inteiro. Todos esses valores encontrados 
# serão retornados em uma nova lista que deve estar ordenada.

def transforma_lista(lista):
    lista_inteiros = []
    for item in lista:
        if item.isdecimal():
            lista_inteiros.append(int(item))
    lista_inteiros.sort()
    return lista_inteiros


lista = ['12', '1213r', '6', '8', '100', '3dd']

print(transforma_lista(lista))

# 11 - Leia por input sua data de nascimento no formado Dia/Mês/Ano e 
# mostre quantos dias você já viveu.

import datetime

data_txt = input("Digite a data em que você nasceu em formato dia/mês/ano: ")
data_nascimento = datetime.datetime.strptime(data_txt, '%d/%m/%Y')
data_agora = datetime.datetime.now()
diferenca_datas = data_agora - data_nascimento
print("Você já vivieu ", diferenca_datas, ' dias')

# 12 - Leia por input sua próxima data de aniversario no formado Dia/Mês/Ano 
# e mostre quantos dias faltam para seu próximo aniversario.

import datetime

data_txt = input("Digite a data do seu próximo aniversário no formato dia/mes/ano")
data_aniversario = datetime.datetime.strptime(data_txt, '%d/%m/%Y')
data_agora = datetime.datetime.now()
diferenca_datas = data_aniversario - data_agora
print("Você fará aniversário daqui ", diferenca_datas.days, ' dias')
