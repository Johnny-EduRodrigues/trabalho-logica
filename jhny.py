lista_primo = []
total_primo = 0
total_numeros = 0
lista_dos_numeros = []
total_numeros_somados = 0
menor_numero = float("inf")
maior_numero = -2
numeros_primos = 0
while True:
    numero = int(input("Número: "))
    if numero < 0:
        break
    else:
        total_numeros += 1
        lista_dos_numeros.append(numero)
        total_numeros_somados += numero
        if numero > maior_numero:
            maior_numero = numero
        if numero < menor_numero:
            menor_numero = numero
    if numero %2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é ìmpar")
    if numero % 3 == 0:
        print(f"{numero} é divisível por 3")
    else: 
        print(f"{numero} não é divisível por 3")
    if numero >= 200 and numero <= 400:
        print(f"{numero} está entre 200 e 400")
    for i in range(1, numero+1):
        if numero % i == 0:
            total_primo += 1
    if total_primo > 2:
        print(f"{numero} não é primo")
        for i in range(1, numero+1):
            if numero % i == 0:
                lista_primo.append(i)
        print(f"Os divisores de {numero} são: {lista_primo}")
    elif total_primo <= 2:
        print("O número é primo")
        numeros_primos += 1
        maior_numero_primo = -2
        menor_numero_primo = float("inf")
        if numero > maior_numero_primo:
            numero = maior_numero_primo
        elif numero < menor_numero_primo:
            numero = menor_numero_primo
    if numero % 5 == 0 and numero % 7 == 0:
        print(f"{numero} é divisível por 5 e por 7 simultaneamente")
    else:
        print(f"{numero} não é divisível por 5 e por 7 simultaneamente")
print(f"Todos os números informados são: {lista_dos_numeros}, foram informados {total_numeros} números.")
print(f"A média aritmética dos seus números é: {total_numeros_somados/total_numeros}")
print(f"O maior número informado é: {maior_numero}, e o menor é {menor_numero}")
if numeros_primos > 0:
    print(f"O maior número primo é {maior_numero_primo}")
    print(f"O menor número primo é {menor_numero_primo}")
total_fatorial = 1
for i in range(1, menor_numero):
    total_fatorial *= i
print(f"O fatorial de {menor_numero} é {total_fatorial}")





            
