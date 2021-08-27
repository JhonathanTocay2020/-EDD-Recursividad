def suma_armonica(numero):
    if numero < 2:
        return 1
    else:
        return 1/numero + suma_armonica(numero-1)

def print_hi(name):
    print("Recursividad Suma Armonica")
    print("El Resultado para una suma armonica n = 7 es: ")
    resultado = suma_armonica(7)
    print(resultado)

if __name__ == '__main__':
    print_hi('PyCharm')
