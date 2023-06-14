from cosas import Alumno, Perro

def main():
    al1 = Alumno("Brayan", 22,"ICO")
    print(vars(al1))
    al1.__nombre = "Areli"
    print(vars(al1))
    al1.__nombre = "Uriel"
    print(vars(al1))
    print("----to string----")
    print(al1)
    al1.set__edad(999)
    print(al1)
    al1.estudiar(4)
    print("--PERRO--")
    perro1 = Perro("poddle", 2, 0.35)
    print(vars(perro1))
    perro1.raza = "De la calle" #set estilo python
    print(vars(perro1))
    perro1.__raza = "schanuzer"
    print(vars(perro1))
    perro1.edad= 12
    perro1.estatura= 0.43
    print(perro1)
    cachorro = Perro.es_cachorro(perro1.edad)
    print(cachorro)
    Perro.dormir()
    danes= Perro.perro_grande(0.8)
    print(danes)
main()
