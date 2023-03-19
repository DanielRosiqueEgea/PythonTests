from Crypto.Cipher import Salsa20
import os

# # Función para cifrar una carpeta
# def cifrar_carpeta(origen, destino, clave):
#     # Inicializar un objeto AES con la clave de cifrado
    
#     cifrador = AES.new(clave, AES.MODE_CBC, 'This is an IV456')

#     # Recorrer cada archivo de la carpeta de origen y cifrarlo
#     for archivo in os.listdir(origen):
#         # Leer el contenido del archivo
#         with open(os.path.join(origen, archivo), 'rb') as f:
#             contenido = f.read()

#         # Añadir relleno al contenido para que tenga una longitud múltiplo de 16 bytes
#         contenido += b'\0' * (AES.block_size - len(contenido) % AES.block_size)

#         # Cifrar el contenido del archivo y escribirlo en el archivo de destino
#         with open(os.path.join(destino, archivo), 'wb') as f:
#             f.write(cifrador.encrypt(contenido))

# # Función para descifrar una carpeta
# def descifrar_carpeta(origen, destino, clave):
#     # Inicializar un objeto AES con la clave de descifrado
#     descifrador = AES.new(clave, AES.MODE_CBC, 'This is an IV456')

#     # Recorrer cada archivo de la carpeta de origen y descifrarlo
#     for archivo in os.listdir(origen):
#         # Leer el contenido del archivo cifrado
#         with open(os.path.join(origen, archivo), 'rb') as f:
#             contenido_cifrado = f.read()

#         # Descifrar el contenido del archivo y escribirlo en el archivo de destino
#         with open(os.path.join(destino, archivo), 'wb') as f:
#             f.write(descifrador.decrypt(contenido_cifrado).rstrip(b'\0'))

# Ejemplo de uso
clave = b'R5xQpGX8mGtbAzxL'  # Clave de cifrado/descifrado
origen = '/NECROTEST'
destino = '/NECROPRUEBA'


# Cifrar la carpeta
# cifrar_carpeta(origen, destino, clave)
key = b'0123456789012345'
cipher = Salsa20.new(key)
ciphertext =  cipher.encrypt(b'The secret I want to send.')
ciphertext += cipher.encrypt(b'The second part of the secret.')
nonce = cipher.nonce

print(ciphertext)

cipher = Salsa20.new(key, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)
print(plaintext)
# Descifrar la carpeta
# descifrar_carpeta(destino, origen + '_descifrado', clave)