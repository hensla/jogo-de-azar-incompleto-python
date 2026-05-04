import random

chance = 1
a = random.randint(1, 100)

num = int(input("Tente acertar o número secreto de 1 a 100: "))
print(a)

while num != a:
    chance += 1
    if num > a:
        num = int(input("Você errou! O numero correto é menor, insira outro: "))
    elif num < a:
        int(input("Você errou! O numero correto é maior, insira outro: "))
print(f"Parabens, você acertou em {chance} tentativas.")
 