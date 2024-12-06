# variaveis
lista_primo = []
total_primo = 0
total_numeros = 0
lista_dos_numeros = []
total_numeros_somados = 0
menor_numero = float("inf")
maior_numero = -2
numeros_primos = 0
maior_numero_primo = -2
menor_numero_primo = float("inf")

#laçode repetição
while True:
    while True:
        try:
            numero = int(input("Número: "))
            break
        except ValueError:
            print("O valor digitado não é um número inteiro")
            continue
    if numero < 0 and total_numeros == 0:
        print("Erro, você deve digitar um número válido antes de terminar o código") 
    if numero < 0:
        break
    else:
        total_numeros += 1 #atualizar o total de números
        lista_dos_numeros.append(numero)# dicionar o número para a lista
        total_numeros_somados += numero  # somar o número 
        # verificar o maior numero e o menor
        if numero > maior_numero:
            maior_numero = numero
        if numero < menor_numero:
            menor_numero = numero
    #verificar se o numero é par ou impar
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é ìmpar")
    # divisivel por 3
    if numero % 3 == 0:
        print(f"{numero} é divisível por 3")
    else: 
        print(f"{numero} não é divisível por 3")
    #Numero > 200 e < 400
    if numero >= 200 and numero <= 400:
        print(f"{numero} está entre 200 e 400")
    # ver se o numero é primo
    total_primo = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            total_primo += 1
    if total_primo > 2:
        print(f"{numero} não é primo")
        #ver os divisores do número
        lista_primo.clear()#limpa a lista de divisores do numero anterior
        for i in range(1, numero + 1):
            if numero % i == 0:
                lista_primo.append(i)
        print(f"Os divisores de {numero} são: {lista_primo}")
    elif total_primo <= 2:
        print("O número é primo")
        numeros_primos += 1
        #atualizar maior e menor numero primo
        if numero > maior_numero_primo:
            maior_numero_primo = numero
        if numero < menor_numero_primo:
            menor_numero_primo = numero
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

#calcular o fatorial do menor número
total_fatorial = 1
for i in range(1, menor_numero + 1):
    total_fatorial *= i
print(f"O fatorial de {menor_numero} é {total_fatorial}")

# calcular o numero com maior frequência
mais_frequente = None
maior_frequencia = 0
for i in lista_dos_numeros:
    frequencia = lista_dos_numeros.count(i)
    if frequencia > maior_frequencia:
        mais_frequente = i
        maior_frequencia = frequencia
print(f"O número mais frequente é {mais_frequente}, aparecendo {maior_frequencia} vezes!")

# i mprimir valor central
if total_numeros % 2 != 0:
    print(f"O número central enviado pelo usuário é {lista_dos_numeros[total_numeros//2]}")#eu n preciso colocar total_numeros //2 +1 pq a contagem nas listas começa pelo 0
else:
    numero1 = lista_dos_numeros[total_numeros // 2 - 1]
    numero2 = lista_dos_numeros[total_numeros // 2]
    media = (numero1 + numero2) / 2
    print(f"O número central enviado pelo usuário é {media}")