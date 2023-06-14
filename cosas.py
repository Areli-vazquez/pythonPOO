class Alumno:
    facultad = "FES Aragon"

    def __int__(self, nom, ed, carr):
        #print("constructor")
        #print(type(self))
        self.__nombre = nom
        self.__edad = ed
        self.__carrera = carr