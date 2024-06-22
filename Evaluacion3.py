variable = input('Ingrese una cadena: ')

def conteo(cadena:str):
    if len(cadena) != 0:
        if len(cadena) == 1:
            print(cadena[0])
        else:
            contador = 1
            caracter = cadena[0]
            for current in cadena[1:]:
                if caracter == current:
                    contador += 1
                else:
                    break
            
            if contador > 1:
                print(contador, end='')
            else:
                print(caracter, end='')

            conteo(cadena[contador:])

conteo(variable)

