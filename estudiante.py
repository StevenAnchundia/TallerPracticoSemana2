class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera


    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Carrera:", self.carrera)

    def saludar(self):
        print(f"Hola, soy {self.nombre} y estudio {self.carrera}.\n")

estudiante1 = Estudiante("Steven", 20, "Ingeniería en Sistemas")
estudiante2 = Estudiante("María", 21, "Arquitectura")

print("===== Estudiante 1 =====")
estudiante1.mostrar_datos()
estudiante1.saludar()

print("===== Estudiante 2 =====")
estudiante2.mostrar_datos()
estudiante2.saludar()
