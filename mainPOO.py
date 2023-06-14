from cosas import Alumno

def main():
    """
    al1 = Alumno()
    print(al1)
    al2 = Alumno()
    print(al1.facultad)
    print(al2.facultad)
    print(Alumno.facultad)
    print("----")
    Alumno.facultad = "FES Aragon EDOMEX"
    print(al1.facultad)
    print(al2.facultad)
    print(Alumno.facultad)
    print("--Un vistazo a los objetos--")
    print(vars(al1))
    print(vars(al2))
    print("--Modificar atributos publicos--")
    al1.__edad = 999
    print(vars(al1))
    print(vars(al2))
    """
    al1 = Alumno("Areli", 24, "ICO")
    al2 = Alumno("Brayan", 22, "ICO")
    print(vars(al1))
    al1.__edad =333
    print(al1.__edad)
    print(vars(al1))
    print(vars(al2))
    #print(al1.facultad)
    #print(al2.__nombre)
    #print(al2.facultad)
main()