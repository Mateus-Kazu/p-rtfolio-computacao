import random

numero_secreto = random.randint(1, 10)
tentativas = 0
print("Adivinhe o número entre 1 e 10")

while True:
    chute = int(input("Seu palpite: "))
    tentativas += 1
    if chute == numero_secreto:
        print(f"Acertou em {tentativas} tentativa(s)!")
        break
    elif chute < numero_secreto:
        print("Muito baixo. Tente novamente.")
    else:
        print("Muito alto. Tente novamente.")
