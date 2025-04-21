var1 = "A"
var2 = "AB"
cont = 0
palavra = "A"

def contar_A(palavra):
    return palavra.count("A")

print(f"N{cont} - {palavra} | A = {contar_A(palavra)} ângulos retos")

while cont < 10: 
    if cont == 0:
        palavra = var2
    else:
        palavra = var2 + var1
        var1 = var2
        var2 = palavra
    cont = cont + 1
    print(f"N{cont} - {palavra} | A = {contar_A(palavra)} ângulos retos")

