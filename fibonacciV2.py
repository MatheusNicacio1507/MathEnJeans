var1 = "A"
var2 = "AB"
cont = 0
palavra = "A"

while cont < 1:  # Ajuste o valor de P aqui (p+1)
    if cont == 0:
        palavra = var2
    else:
        palavra = var2 + var1
        var1 = var2
        var2 = palavra
    cont += 1

import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.tracer(0)

t.hideturtle()
t.speed(0)
t.penup()
t.goto(-650, -300)
t.pendown()
t.left(90)

def contar_letras(palavra):
    contagem = {}
    for letra in palavra:
        if letra in contagem:
            contagem[letra] += 1
        else:
            contagem[letra] = 1
    return contagem

def posicoes_letras(palavra):
    for i, letra in enumerate(palavra):
        posicao = i + 1
        par_ou_impar = "par" if posicao % 2 == 0 else "ímpar"

        if letra == "A":
            t.pencolor("black")  # Linha preta para A
            if posicao % 2 == 0:
                t.left(90)
            else:
                t.right(90)
        else:
            t.pencolor("red")  # Linha vermelha para B

        t.forward(20)
        print(f"Letra '{letra}' está na posição {posicao} ({par_ou_impar})")

posicoes_letras(palavra)

screen.update()
turtle.done()
