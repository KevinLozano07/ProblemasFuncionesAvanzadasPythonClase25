#Modifica el programa para que también te permita dividir el total a pagar entre el número de personas que compartirán la cuenta.

print("")
Numero_personas = int(input("¿Cuantas personas entraron a comer? "))

def calcular_propina(total_cuenta, porcentaje_propina):
    propina = total_cuenta * (porcentaje_propina / 100)
    total_pagar = total_cuenta + propina
    return propina, total_pagar

# Ejemplo de uso
print("")
total_cuenta = float(input("Ingresa el total de la cuenta: "))
print("")
porcentaje_propina = float(input("Ingresa el porcentaje de propina que deseas dejar: "))
print("")
print("-" * 100)
print("")

propina, total_pagar = calcular_propina(total_cuenta, porcentaje_propina)

if Numero_personas == 1:
 print(f"Debes dejar una propina de: ${propina:.2f}")
 print("")
 print(f"El total a pagar es: ${total_pagar:.2f}")
 print("")
 print("-" * 100)
 print("")
else:
 Pago_individual = total_pagar / Numero_personas
 print(f"Debes dejar una propina de: ${propina:.2f}")
 print("")
 print(f"Cada uno debe pagar una canidad individual de: ${Pago_individual:.2f}")
 print("")
 print(f"El total a pagar es: ${total_pagar:.2f}")
 print("")
 print("-" * 100)
 print("")