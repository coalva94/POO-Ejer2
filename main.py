from administrative import Administrative
from engineer import Enginer
from manager import Manager
def main():
    administrative = Administrative('Juan', 25, 1000.12, 'RRHH')
    enginer = Enginer('Pedro', 30, 1025.50, 'Sistemas')
    manager = Manager('Maria', 35, 1500.75, 'Losgistica')

    print("Información del administrativo: ")
    administrative.mostrar_info()

    print("\nInformación del ingeniero: ")
    enginer.mostrar_info()

    print("\nInformación del manager: ")
    manager.mostrar_info()

main()
