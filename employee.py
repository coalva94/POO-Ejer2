#Creación de clase base empleado
class Employee:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

#mostrar_info(): Muestra la información del empleado.
    def mostrar_info(self):
        print(f'Nombre: {self.nombre}')
        print(f'Edad: {self.edad}')
        print(f'Salario: {self.salario}')
