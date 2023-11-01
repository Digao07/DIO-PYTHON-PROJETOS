# Trabalhando com listas
# Podem armazenar de maneira sequencial qualquer tipo de objeto
# Tem como método de criação o construtor list, a função range ou valores separados por vírgula dentro de colchetes
# São mutáveis, podendo alterar os valores após sua criação

# Criando uma lista
frutas = ["laranja", "uva", "maca"]
print(frutas)

# Criando uma lista vazia
objetos = []
print(objetos)

# Criando através de um construtor
# Através de um elemento iterável que são os caracteres
# Neste caso ele cria uma lista com os caracteres que estão dentro das aspas
letras = list("python")
print(letras)

# Criando um construtor para números através do range
# Lista pelo qual estará contido os valores de 0 a 9
numeros = list(range(10))
print(numeros)

# Criando uma lista com elementos diversos iteráveis
# Contém inteiros, strings e booleano
# Criado uma lista com atributos de um carro
carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)