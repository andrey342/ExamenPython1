import random

def encontrar_menores(diccionario,letra):
    """Dado un diccionario de palabras, y una letra, esta función devuelve la lista de palabras que empiezan por una letra que alfabéticamente está antes que la indicada.
    Args:
      diccionario
      letra
    Returns:
      resultado: ej. ['AUNQUE','ABINAR']
    """

    # 1. el error se debe a que resultado = [] estaba dentro del bucle y del if , por lo que cada vez que comprobaba una letra menor que "b" por ejemplo
    # se guardaba en la lista pero la sigueinte comprobacion de la letra se vacia otra vez, por lo tanto se iba vaciando con cada loop.
    # 2. la solucion ha sido sacarlo fuera del for general para que no se vacie cada vez que encuentre una letra anterior a la que nos han dado

    resultado=[]
    for clave in diccionario:
        
        for palabra in diccionario[clave]:
            
            if palabra[0] < letra:
                # se ha quitado esta linea
                #resultado=[]
                resultado.append(palabra)
    
    return resultado

def add_client(clients_list,nif,name,address,phone,email):
    """Dado un diccionario de clientes y datos de un nuevo cliente, esta función inserta estos datos como un nuevo cliente.
    Args:
      diccionario
      nif
      name 
      address
      phone
      email
    """
    # 1. el error se debe a que dentro del diccioanrio le declarabamos otro , nif : {}... entonces tenemos uno dentro de otro
    # se ha quitado la declaracion del que esta dentro del diccionario ya que el primer diccionario ya tiene el nif del cliente , no hace falta hacerle otro dentro
    # 2. se ha solucionado quitando la declaracion del que esta dentro nif: {} 
    clients_list[nif] = {
        'name': name,
        'address': address,
        'phone': phone,
        'email': email
        
    }


def repartir_cartas(cartas_iniciales,repeticiones):
    """Dada una baraja de cartas iniciales y un número de repeticiones, esta función selecciona 5 cartas aleatorias de esta baraja y las mete en un diccionario llamado combinaciones. El proceso se repite tantas veces como repeticiones se indiquen.
    Args:
      cartas_iniciales
      repeticiones
    Returns:
      combinaciones: ej. {'repeticion1': ['contable', 'alguacil', 'asesino', 'cardenal', 'obispo']}
    """    

    # 1. el error ha sido que cartal_aleatorias estaba vacia ya que en la linea cartas_aleatorias.remove(carta) que estaba dentro del for que se recorre 4 veces 0-5
    # entonces la carta se remueve varias veces con cada repeticion
    # 2. la solucion ha sido declarar carta fuera y cartas_aleatorias.remove(carta) dejar fuera del segundo for ya que como en remove estaba dentro del for
    # la carta se removia con cada repeticion y al final no queda ninguna


    combinaciones={}
    carta = ""
    for i in range(1,repeticiones+1):
        cartas_aleatorias = cartas_iniciales 
        combinaciones["repeticion"+str(i)]=[]

        for j in range(0,5):
            carta=random.choice(cartas_aleatorias)
            combinaciones["repeticion"+str(i)].append(carta)
        # esto fuera del segundo bucle
        cartas_aleatorias.remove(carta)

    return combinaciones


    
