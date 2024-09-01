def cifrado_cesar(texto, corrimiento):
    resultado = ""

    for char in texto:
        if char.isalpha():
            # Determinar si el carácter es mayúscula o minúscula
            ascii_offset = 65 if char.isupper() else 97
            # Realizar el corrimiento y asegurarse de que esté dentro del rango alfabético
            char_cifrado = chr((ord(char) - ascii_offset + corrimiento) % 26 + ascii_offset)
            resultado += char_cifrado
        else:
            # Si el carácter no es una letra, se añade tal cual
            resultado += char

    return resultado

# Ejemplo de uso
#texto_a_cifrar = input("Ingresa el texto a cifrar: ")
#corrimiento = int(input("Ingresa el corrimiento: "))
#texto_cifrado = cifrado_cesar(texto_a_cifrar, corrimiento)
#print("Texto cifrado:", texto_cifrado)