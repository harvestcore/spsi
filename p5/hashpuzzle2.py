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
    
    token = random.randint(0, 9)

    #   Mientras no encuentre el hash correcto
    while not found:
        #   Aumento el número de intentos
        ntry += 1

        if ntry > 1:
            #   Sumo 1 al token
            token += 1

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


def ej7():
    #   Creo y abro un archivo .csv para almacenar los datos
    with open('ej7.csv', 'w', newline='') as f:
        fieldnames = ['bloque', 'cadena', 'hash', 'zeros', 'intentos']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        #   Mensaje
        msj = 'angel'

        #   Cadena k aleatoria
        cadenaK = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(10))
        
        #   Nº de bits a buscar
        b = 1

        #   Iteraciones a calcular
        for x in range(20):
            for i in range(10):
                data = findZeros(msj, b, cadenaK)
                cadenaK = data['hash']
                writer.writerow(data)

            b += 1

if __name__ == '__main__':
    ej7()
    