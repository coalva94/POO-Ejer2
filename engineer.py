'''Clase Derivada: Ingeniero
Hereda de: Empleado
Atributos adicionales:
especialidad (cadena)
Métodos:
mostrar_info(): Muestra la información del ingeniero, incluyendo la especialidad.
'''
from employee import Employee
class Enginer(Employee):
    def __init__(self, nombre, edad, salario,especialidad):
        super().__init__(nombre, edad, salario)
        self.especialidad = especialidad

    def mostrar_info(self):
        super().mostrar_info()
        print(f'Especialidad: {self.especialidad}')
        
