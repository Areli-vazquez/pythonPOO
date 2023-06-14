# if
edad = 20
if edad >= 18:
    print("Eres mayor de edad.")

# if-esle

edad = 15
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# if- elif - else
edad = 20
if edad < 13:
    print("Eres un niño.")
elif edad < 18:
    print("Eres un adolescente.")
else:
    print("Eres un adulto.")

# if-elif-elif
edad = 20
if edad < 13:
    print("Eres un niño.")
elif edad < 18:
    print("Eres un adolescente.")
elif edad < 30:
    print("Eres un joven adulto.")

# For   for(int = 1 ; i<10 ; i++)

for i in range(1, 10, 1):
    print(i)

frutas = ['piña', 'pera', 'manzana', 'fresa', 'aguacate']
for numero in frutas:
    print(numero)
print("-----")
#break y continue
for numero in frutas:
    if numero == "manzana":
        break  # ó continue
    print(numero)  # imprime la fruta
print("Fin")

#While
tam = 0
while tam < 10:
    print(tam)
    tam = int(input("Dame un número entero:"))
print("Final")

#FUNCIONES
from aritmetica import suma, resta
def main():
    resultado = suma(3, None)
    print(resultado)
    print(resta(b=5, a=3))

main()