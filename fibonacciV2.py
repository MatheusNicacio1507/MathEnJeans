var1 = "A"
var2 = "AB"
cont = 0
palavra = "A"

#---------------CONTROLE---------------------
px = 10 # Mude a escala de pixel aqui
grau = 90 #Mude a angulação aqui
#-------------------------------------------

while cont < 10: #Ajuste o valor de P aqui EX: para P=5 bote o valor de 5
    if cont == 0:
        palavra = var2
    else:
        palavra = var2 + var1
        var1 = var2
        var2 = palavra
    cont = cont + 1  # <- Corrigido: movido para fora do else
 
import turtle
 
t = turtle.Turtle()
 
screen = turtle.Screen()
screen.tracer(0)  # Desliga a atualização automática
 
t.hideturtle()#tira a setinha
t.speed(0)  # velocidade máxima
t.penup()
#t.goto(-650, -300)  # posição no canto superior esquerdo (ajuste conforme o fractal)
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
        t.pencolor("black" if letra == "A" else "red")  # <- Adicionada a troca de cor
        posicao = i + 1
        if posicao % 2 == 0:
            par_ou_impar = "par"
            if letra == "A":
                t.left(grau)
                t.forward(px)#Muda escala de px
            else:
                t.forward(px)#Muda escala de px
        else:
            par_ou_impar = "ímpar"
            if letra == "A":
                t.right(grau)
                t.forward(px)#Muda escala de px
            else:
                t.forward(px)#Muda escala de px
        print(f"Letra '{letra}' está na posição {posicao} ({par_ou_impar})")
        print(palavra)
posicoes_letras(palavra)
 
screen.update()
turtle.done()
