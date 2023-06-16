from cosas import *

def main():
    per1 = Persona("Uriel", 19)
    print(per1)
    print(Persona.descripcion)
    print("-----HERENCIA ALUMNO-----")
    al1 = Alumno("Areli", 24, "1233456","ICO")
    print(al1)
    print(Alumno.descripcion)
    al2 = Alumno.constructor_defecto()
    print(al2)
    al2.nombre = "Buarel"
    print(al2)
    al2.dormir()
    print("---HRENCIA PROFE---")
    profe1 = Profesor("Jesus" , 30 +16, 12345, "Ingeniería de software")
    print(profe1)
    profe1.dormir()
    print("---HERENCIA AYUDANTE PROFE---")
    ayudante = AyudanteProfesor("Monse" , 20, "23232","ICO",2323, "ing.software", 4)
    ayudante.dormir()
    ayudante.nombre = "Abraham"
    ayudante.dar_clase("P.O.O")

main()