# Valores do primeiro dia de cada mes e dos dias da semana
primeiro_mes = "ADDGBEGCFADF"
dias = ["Domingo", "Segunda", "Terca", "Quarta", "Quinta", "Sexta", "Sabado"]

# Passa uma letra maiuscula para numero de 1 a 7
def letra_para_num(letra):
    return ord(letra) - ord("A") + 1

# Passa um numero de 1 a 7 para dia da semana
def num_para_dia(num):
    return (dias[num - 1])

# Escreve um dia formatado
def print_dia(dia, mes, ano):
    print("Dia {}/{}/{}".format(dia, mes, ano))

# Verifica se e bissexto
def eh_bissexto(ano):
    return ((ano % 400 == 0) or ((ano % 100 != 0) and (ano % 4 == 0)))

# Calcula o dia da semana
def calcula_dia_semana(dia, mes, ano):
    # Escrita do dia original
    print_dia(dia, mes, ano)

    regressoes = (ano - 1) + (ano//4) - (ano//100) + (ano//400)
    n = 7 - regressoes % 7

    # Restante calculo, comum a ambos os calendarios
    r = letra_para_num(primeiro_mes[mes - 1]) + dia
    c = 1 + (r - 2) % 7

    if (eh_bissexto(ano) and mes in (1, 2)):
        w = 1 + (c - n + 6) % 7

    else:
        w = 1 + (c - n + 7) % 7

    return num_para_dia(w)

# New code (above was code i had already made in another project)

total = 0

for ano in range(1901,2001):
    for mes in range(1,13):
        if calcula_dia_semana(1, mes, ano) == "Domingo":
            total += 1

print(total)
