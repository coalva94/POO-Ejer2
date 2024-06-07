'''Clase Derivada: Administrativo
Hereda de: Empleado
Atributos adicionales:
seccion (cadena)
Métodos:
mostrar_info(): Muestra la información del administrativo, incluyendo la sección.'''

from employee import Employee

class Administrative(Employee):
    def __init__(self, nombre, edad, salario,seccion):
        super().__init__(nombre, edad, salario)
        self.seccion = seccion

    def mostrar_info(self):
        super().mostrar_info()
        print(f'Sección: {self.seccion}')
