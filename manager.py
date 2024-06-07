'''Clase Derivada: Manager
Hereda de: Empleado
Atributos adicionales:
departamento (cadena)
Métodos:
mostrar_info(): Muestra la información del manager, incluyendo el departamento.
'''
from employee import Employee

class Manager(Employee):
    def __init__(self, nombre, edad, salario,departamento):
        super().__init__(nombre, edad, salario)
        self.departamento = departamento

    def mostrar_info(self):
        super().mostrar_info()
        print(f'Deparatamento: {self.departamento}')
