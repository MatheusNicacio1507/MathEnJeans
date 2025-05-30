var1 = "A"
var2 = "AB"
cont = 0
palavra = "A"
print(f"N{cont}-{palavra}")
 
while cont < 20: #Ajuste o valor de P aqui (p+1) EX: para P=5 bote o valor de P=6
    if cont == 0:
        palavra = var2
    else:
        palavra = var2 + var1
        var1 = var2
        var2 = palavra
    cont = cont + 1  # <- Corrigido: movido para fora do else
    print(f"N{cont}-{palavra}")
