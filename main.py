numeroParaMultiplicar = int(input("¿Cual Tabla de multiplicar quieres? "))

contador = 0

while contador < 13:
    resultado = numeroParaMultiplicar * contador
    print(f"{numeroParaMultiplicar} x {contador} = {resultado}")
    contador = contador + 1