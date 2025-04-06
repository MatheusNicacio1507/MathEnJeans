var1 = "A"
var2 = "AB"
acu = 0
cont = 1
palavra = "AAB"
 
while cont < 17: #Ajuste o valor de P aqui (p+1) EX: para P=5 bote o valor de P=6
  acu = var2 + var1
  var1 = var2
  var2 = acu
  palavra += acu
  cont = cont + 1
 
import turtle
 
t = turtle.Turtle()

screen = turtle.Screen()
screen.tracer(0)  # Desliga a atualização automática

t.hideturtle()#tira a setinha
t.speed(0)  # velocidade máxima
t.penup()
t.goto(-650, -300)  # posição no canto superior esquerdo (ajuste conforme o fractal)
t.pendown()
 
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
        if posicao % 2 == 0:
            par_ou_impar = "par"
            if letra == "A":
                t.left(90)
                t.forward(1)#Muda escala de px
            else:
                t.forward(1)#Muda escala de px
        else:
            par_ou_impar = "ímpar"
            if letra == "A":
                t.right(90)
                t.forward(1)#Muda escala de px
            else:
                t.forward(1)#Muda escala de px
        print(f"Letra '{letra}' está na posição {posicao} ({par_ou_impar})")
 
posicoes_letras(palavra)

screen.update()
turtle.done()
