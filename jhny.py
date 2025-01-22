# Variáveis
lista_primo = []  # Lista dos divisores do número que não é primo
total_primo = 0  # Número total de números primos
total_numeros = 0  # Número total de todos os números informados
lista_dos_numeros = []  # Lista que contém todos os números informados
total_numeros_somados = 0  # Soma de todos os números informados
menor_numero = float("inf")  # Variável que vai armazenar o menor número informado
maior_numero = -2  # Variável que vai armazenar o maior número informado
numeros_primos = 0  # Total dos números primos
maior_numero_primo = -2  # Inicializa o maior número primo
menor_numero_primo = float("inf")  # Inicializa o menor número primo
mais_frequente = []  # Lista que vai receber os números e calcular o mais frequente
maior_frequencia = 0  # Vai receber a maior frequência

# Funções
def parOuImpar(numero):
    if numero % 2 == 0:
        print(f"{numero} é Par")
    else:
        print(f"{numero} é Ímpar")


def divisivelPor3(numero):
    if numero % 3 == 0:
        print(f"{numero} é divisível por 3")
    else:
        print(f"{numero} não é divisível por 3")


def verificarNumeroPrimo(numero):
    global maior_numero_primo, menor_numero_primo, numeros_primos

    total_primo = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            total_primo += 1

    if total_primo > 2:
        print(f"{numero} não é primo")

        # Ver os divisores do número
        lista_primo.clear()  # Limpa a lista de divisores do número anterior
        for i in range(1, numero + 1):
            if numero % i == 0:
                lista_primo.append(i)  # Vai adicionar o divisor do número na lista
        print(f"Os divisores de {numero} são: {lista_primo}")
    else:
        print(f"O número {numero} é primo")
        numeros_primos += 1

        # Atualizar maior e menor número primo
        if numero > maior_numero_primo:
            maior_numero_primo = numero
        if numero < menor_numero_primo:
            menor_numero_primo = numero


def fatorial(numero):
    total_fatorial = 1
    for i in range(1, numero + 1):
        total_fatorial *= i 
    print(f"O fatorial de {numero} é {total_fatorial}")


def mais_frequente():
    global maior_frequencia, mais_frequente
    for i in lista_dos_numeros:
        frequencia = lista_dos_numeros.count(i)
        if frequencia > maior_frequencia:
            mais_frequente = [i]
            maior_frequencia = frequencia
        elif frequencia == maior_frequencia and i not in mais_frequente:
            mais_frequente.append(i)
    print(f"Os números mais frequentes são {mais_frequente}, aparecendo {maior_frequencia} vezes!")


def valorCentral():
    if total_numeros % 2 != 0:
        print(f"O número central enviado pelo usuário é {lista_dos_numeros[total_numeros//2]}")  # Eu não preciso colocar total_numeros //2 + 1 porque a contagem nas listas começa pelo 0
    else:
        numero1 = lista_dos_numeros[total_numeros // 2 - 1]
        numero2 = lista_dos_numeros[total_numeros // 2]
        media = (numero1 + numero2) / 2
        print(f"O número central enviado pelo usuário é {media}")


# Laço de repetição
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
        total_numeros += 1  # Atualizar o total de números
        lista_dos_numeros.append(numero)  # Adicionar o número à lista
        total_numeros_somados += numero  # Somar o número

        # Verificar o maior número e o menor
        if numero > maior_numero:
            maior_numero = numero
        if numero < menor_numero:
            menor_numero = numero

    # Verificar se o número é par ou ímpar
    parOuImpar(numero)

    # Divisível por 3
    divisivelPor3(numero)

    # Número entre 200 e 400
    if numero >= 200 and numero <= 400:
        print(f"{numero} está entre 200 e 400")

    # Verificar se o número é primo
    verificarNumeroPrimo(numero)

    # Verificar se o número é divisível por 5 e por 7
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

# Calcular o fatorial do menor número
fatorial(menor_numero)

# Calcular o número com maior frequência
mais_frequente()

# Imprimir valor central
valorCentral()
