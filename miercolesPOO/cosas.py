class Alumno:
    facultad = "FES Aragón"

    def __init__(self, nom, ed, carr):
        self.__nombre = nom
        self.__edad = ed
        self.__carrera = carr

    def set_nombre(self, nom):
        self.__nombre = nom

    def get_nombre(self):
        return self.__nombre

    def set__edad(self, ed):
        if ed >= 8 and ed < 120:
            self.__edad = ed
        else:
            print("La edad no es correcta")
            self.__edad = 0

    def get_edad(self):
        return self.__edad

    def set_carrera(self, carr):
        self.__carrera = carr

    def get_carrera(self):
        return self.__carrera

    def __str__(self):
        cadena = "Nombre: " + self.__nombre
        cadena = cadena + "\n Edad: " + str(self.__edad)
        cadena = cadena + "\n Carrera: " + self.__carrera
        cadena = cadena + "\n ----------"
        return cadena

    def estudiar(self, horas=1):
        print(f"El alumno {self.__nombre} esta estudiando por {horas} horas")

class Perro:
    reino = "Canino"

    def __init__(self, raza, edad, estatura):
        self.__raza = raza
        self.__edad = edad
        self.__estatura= estatura

    #Método de acceso get
    @property
    def raza(self):
        return self.__raza

    #Método de acceso set
    @raza.setter
    def raza(self, la_raza):
        self.__raza = la_raza

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, la_edad):
        if la_edad >0 and la_edad < 20:
            self.__edad = la_edad
        else:
            print("Esa no es una edad válida")
            self.__edad= 0

    @property
    def estatura(self):
        return self.__estatura

    @estatura.setter
    def estatura(self, la_estatura):
        if la_estatura > 0.1 and la_estatura < 1.1:
            self.__estatura = la_estatura
        else:
            print("No WAAAAY! :0")
            self.__estatura = 0.1

    def __str__(self):
        return f"""
        ---------------
        Raza: {self.__raza}
        Edad: {self.__edad}
        Estatura: {self.__estatura}
        ---------------
        """

    @staticmethod
    def es_cachorro(edad):
        return edad < 13

    @staticmethod
    def dormir(veces= 5):
        for n in range(veces):
            print(f"Dando vuelta { n + 1}")
        print("ZzZzZzZ")

    @classmethod
    def perro_grande(cls,est):
        if est > 0.79:
            return cls("",0,est)