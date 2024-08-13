def convertir_temperatura(valor, unidad_origen, unidad_destino):
    if unidad_origen == "Celsius" or unidad_origen == "celsius":
        if unidad_destino == "Fahrenheit" or unidad_destino == "fahrenheit":
            return (valor * 9/5) + 32
        elif unidad_destino == "Kelvin" or unidad_destino == "kelvin":
            return valor + 273.15
        elif unidad_destino == "Rankine" or unidad_destino == "rankine":
            return (1.8 * valor) + 491.67
        
    elif unidad_origen == "Fahrenheit" or unidad_origen == "fahrenheit":
        if unidad_destino == "Celsius" or unidad_destino == "celsius":
            return (valor - 32) * 5/9
        elif unidad_destino == "Kelvin" or unidad_destino == "kelvin":
            return (valor - 32) * 5/9 + 273.15
        elif unidad_destino == "Rankine" or unidad_destino == "rankine":
            return valor +  459.67
        
    elif unidad_origen == "Kelvin" or unidad_origen == "kelvin":
        if unidad_destino == "Celsius" or unidad_destino == "celsius":
            return valor - 273.15
        elif unidad_destino == "Fahrenheit" or unidad_destino == "fahrenheit":
            return (valor - 273.15) * 9/5 + 32
        elif unidad_destino == "Rankine" or unidad_destino == "rankine":
            return valor * 1.8
        
    elif unidad_origen == "Rankine" or unidad_origen == "rankine":
        if unidad_destino == "Celsius" or unidad_destino == "celsius":
            return (valor - 491.67) * 5/9
        elif unidad_destino == "Fahrenheit" or unidad_destino == "fahrenheit":
            return valor -  459.67
        elif unidad_destino == "Kelvin" or unidad_destino == "kelvin":
            return valor * 5/9

# Ejemplo de uso
print("")
valor = float(input("Ingresa el valor de la temperatura: "))
print("")
unidad_origen = input("Ingresa la unidad de origen (Celsius, Fahrenheit, Kelvin, Rankine): ")
print("")
unidad_destino = input("Ingresa la unidad de destino (Celsius, Fahrenheit, Kelvin, Rankine): ")
print("")

resultado = convertir_temperatura(valor, unidad_origen, unidad_destino)

print(f"{valor} {unidad_origen} son {resultado:.2f} {unidad_destino}")
print("")