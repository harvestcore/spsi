import hashlib, secrets, time, random, csv, string, codecs

#   Genera cadena aleatoria de bits de tamaño n
def bitGenerator(n):
    cadena = ""

    for i in range(0, n):
        cadena += str(random.randint(0,1))
    
    return int(cadena, base=2)

#   msj = texto
#   b   = nº bits que tienen que ser 0
#   k   = cadena de n bits
def findZeros(msj, b, k):

    #   Nº de bits de la cadena k
    kbits = len(k) * 8
    # print("kbits:", kbits)

    #   ID
    identifier = msj + k
    # print("identifier:", identifier)

    #   Nº intento
    ntry = 0

    #   Cadena encontrada?
    found = False

    #   Data
    data = {}

    #   Mientras no encuentre el hash correcto
    while not found:
        #   Aumento el número de intentos
        ntry += 1

        #   Genero cadena aleatoria de bits
        token = bitGenerator(kbits)
        # print("token:", token)

        #   Creo nuevo identificador usando el anterior y el token generado
        newid = identifier + str(token)

        #   Calculo su hash
        hashed_newid = hashlib.sha256(newid.encode('utf8')).hexdigest()
        
        #   Paso a binario el hash y le quito los 2 primeros bits (que indican que se encuentra en binario)
        binary_hash = bin(int(hashed_newid, 16))[2:].zfill(256)

        #   Si los b primeros caracteres son 0...
        if (int(binary_hash[0:b],2) == 0):
            #   Se ha encontrado el hash
            found = True

            #   Diccionario con la información
            data = {
                'bloque': identifier,
                'cadena': token,
                'hash': hashed_newid,
                'zeros': b,
                'intentos': ntry
            }

    return data


def ej2():
    #   Creo y abro un archivo .csv para almacenar los datos
    with open('ej2.csv', 'w', newline='') as f:
        fieldnames = ['bloque', 'cadena', 'hash', 'zeros', 'intentos']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        #   Mensaje
        msj = 'angel'

        #   Cadena k aleatoria
        cadenaK = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(10))
        
        #   Nº de bits a buscar
        b = 2

        #   Primera iteración
        data = findZeros(msj, b, cadenaK)
        
        #   Guardo el hash encontrado como nueva cadena K
        cadenaK = data['hash']

        #    Escribo datos en el archivo
        writer.writerow(data)

        #   Siguientes 9 iteraciones del blockchain
        for i in range(9):
            data = findZeros(msj, b, cadenaK)
            cadenaK = data['hash']
            writer.writerow(data)

def ej3():
    #   Creo y abro un archivo .csv para almacenar los datos
    with open('ej3.csv', 'w', newline='') as f:
        fieldnames = ['bloque', 'cadena', 'hash', 'zeros', 'intentos']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        #   Mensaje
        msj = 'angel'
        
        #   Hash del último bloque
        cadenaK = '25fc00572525a3ade1f6819cbce7b3673acf586bd7f5985c0878f31b3749e6ea'

        #   Nº de bits a buscar
        b = 3

        #   Siguientes 10 iteraciones del blockchain
        for i in range(10):
            data = findZeros(msj, b, cadenaK)
            cadenaK = data['hash']
            writer.writerow(data)

def ej4():
    #   Creo y abro un archivo .csv para almacenar los datos
    with open('ej4.csv', 'w', newline='') as f:
        fieldnames = ['bloque', 'cadena', 'hash', 'zeros', 'intentos']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        #   Mensaje
        msj = 'angel'

        #   Hash del último bloque
        cadenaK = '0162f293cbe4a906bbe1c70e8ac8a9da79e1439dd53dc4227e2ad37a88c182ad'

        #   Nº de bits a buscar
        b = 3

        #   Siguientes iteraciones del blockchain
        for x in range(20):
            for i in range(10):
                data = findZeros(msj, b, cadenaK)
                cadenaK = data['hash']
                writer.writerow(data)

            b += 1


if __name__ == '__main__':
    ej4()
    