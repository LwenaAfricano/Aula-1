
#1º exercício

mood = input("How are you? ")

if mood == "happy":
    print("It is great to see you happy!")

elif mood == "nervous":
    print("Take a deep breath 3 times.")

elif mood == "excited":
    print("It is great!")

elif mood == "sad":
    print("I am sorry!")

elif mood == "relaxed":
    print("Uhuu!")

else:
    print("I don't recognize this mood")

print()


#2º exercício

secret = 4
guess = int(input("Introduza o seu palpite: "))
if guess != secret:
    print("Infelizmente não conseguiu adivinhar.")

else:
    print("Parabéns! O número secreto é o 4.")

print()


#3º exercício

num1 = int(input("Escolha um número: "))
num2 = int(input("Escolha outro número: "))
operation = input("Escolha uma operação aritmétrica: ")

if operation == "+":
    print("num1 + num2 = " , num1+num2)

elif operation == "-":
    print("num1 - num2 = " , num1-num2)

elif operation == "*":
    print("num1 * num2 = " , num1*num2)

else:
    print("num1 / num2 = " , num1/num2)
