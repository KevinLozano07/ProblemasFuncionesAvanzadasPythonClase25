palabras_positivas = {"bien": 1, "genial": 3, "fantástico": 5, "excelente": 4, "feliz": 2}
palabras_negativas = {"mal": 1, "terrible": 4, "horrible": 5, "malo": 2, "triste": 3}

def analizar_sentimiento(texto):
    texto = texto.lower()
    conteo_positivo = sum(palabras_positivas[palabra] for palabra in palabras_positivas if palabra in texto)
    conteo_negativo = sum(palabras_negativas[palabra] for palabra in palabras_negativas if palabra in texto)

    if conteo_positivo > conteo_negativo:
        return "Sentimiento positivo"
    elif conteo_negativo > conteo_positivo:
        return "Sentimiento negativo"
    else:
        return "Sentimiento neutral"

# Ejemplo de uso
print("")
texto = input("Escribe una oración para analizar: ")
print("")
resultado = analizar_sentimiento(texto)
print(f"El resultado del análisis es: {resultado}")
print("")