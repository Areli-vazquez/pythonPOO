#LUNES 12 DE JUNIO 2023
# Esto es un comentario
print("Hola Mundo")  # Esto imprime "Hola Mundo"

print("Hola", "Mundo")

print("Hola" + "Mundo")

print("Hola", "Mundo", sep="-")  # Imprime: Hola-Mundo

print("Hola", end="")
print("Mundo")  # Imprime: HolaMundo

nombre = "Areli"
carrera = "ICO, la mejor"
print("Mi nombre es {} y estudio {} en la FES Aragón".format(nombre, carrera))

nombre = "Areli"
carrera = "ICO, la mejor"
print(f"Mi nombre es {nombre} y estudio {carrera} en la FES Aragón")

"""
este es
un 
comentario de
múltiple línea
"""

# Operadores aritméticos
suma = 5 + 3  # 8
resta = 5 - 3  # 2
producto = 5 * 3  # 15
division = 5 / 3  # 1.66667
division2 = 5 // 3  # 1
modulo = 5 % 3  # 2
potencia = 5 ** 3  # 125

# Operadores de comparación
igual = 5 == 3  # False
diferente = 5 != 3  # True
mayor_que = 5 > 3  # True
menor_que = 5 < 3  # False
mayor_o_igual_que = 5 >= 3  # True
menor_o_igual_que = 5 <= 3  # False

# Operadores lógicos
y = True and False  # False
o = True or False  # True
no = not True  # False

saludo = "Hola Mundo"
cita = 'Los alumnos de ICO dicen: "Hola Mundo"'
parrafo = """Esto es un párrafo
que abarca varias
líneas"""


def fn_uno():
    print("Hola")


a, b, c = 10, "Hola", [2.3, 3.4]
print(a)
print(b)
print(c[1])

frutas =('limon', 'Aguacate' , 'Fresa')
frutas_dos = ('Aguacate', 'Limón', 'Naranja')

print(frutas)
print(frutas_dos)

#frutas[1] = 'Piña'
#frutas_dos [1] = 'Piña' #no puede ser modificada
print(frutas[1])
print(frutas_dos[0:2:1])
print(frutas_dos[-1])

#Diccionario
alumno = {'num_cuenta': 123456789, 'carrera' : 'ICO',
          'direccion' : {'calle':'rancho seco', 'numero' : 23}
          }
print(alumno['direccion']['calle'][3:6:1])