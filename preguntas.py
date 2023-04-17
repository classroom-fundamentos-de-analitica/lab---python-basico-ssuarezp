"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv

with open('data.csv','r',encoding='UTF-8') as data:
    entrada=csv.reader(data,delimiter=' ')
    lista=list(entrada)

listadef=[]
for linea in lista:
    x=linea[0].split('\t')
    listadef.append(x)

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    csvfile = open("data.csv", "r")
    data = []
    for row in csvfile:
        data.append(int(row[2]))
    sum=0
    for i in data:
        sum+=i    
    return sum

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    from collections import Counter
    csv = open("/content/drive/MyDrive/Asignaturas/2023-1/Fundamentos_Analítica/data.csv", "r")
    letras=[]
    for i in csv:
      letras.append(i[0])
    letras_u=list(set(letras))
    letras_u.sort()
    T=[]
    for j in letras_u:
      T.append((j,letras.count(j)))
    return T

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    lista1 = [z[0] for z in listadef[0:]]
    lista1 = sorted(list(set(lista1)))

    listasum= []
    for i in lista1:
        w = [int(z[1]) for z in listadef[0:] if z[0] == i]
        listasum.append(sum(w))

    listasum = list(zip(lista1,listasum))
    return listasum

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    lista1 = [z[2].split("-") for z in listadef[0:]]
    b = sorted(list(set([z[1] for z in lista1])))

    cuenta = []

    for i in b:
        w = ([z for z in lista1 if z[1] == i])
        cuenta.append(len(w))

    cuenta = list(zip(b,cuenta))

    return cuenta
   
def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    lista1 = [z[0] for z in listadef[0:]]
    lista1 = sorted(list(set(lista1)))

    maxi = []
    mini = []
    for i in lista1:
        w = [int(z[1]) for z in listadef[0:] if z[0] == i]
        maxi.append(max(w))
        mini.append(min(w))

    valor = list(zip(lista1,maxi,mini))
    return valor

  def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    dic1={}
    for row in listadef:
        for i in row[4].split(","):
            currentKeyValue = dic1.get(str(i[:3]),-1)
            currentValue = int(i[4:])
            if(currentKeyValue == -1):
                dic1[str(i[:3])] = (currentValue,currentValue)
            if(currentKeyValue !=-1):
                dic1[str(i[:3])] = (min(currentKeyValue[0],currentValue),max(currentKeyValue[1],currentValue))

    sort = list(sorted(dic1.items()))
    final = []
    for i in sort:
        final.append((i[0],i[1][0],i[1][1]))
    return final

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    dic1 = {}
    for i in listadef:
        index = int(i[1])
        current = dic1.get(index,-1)
        if(current == -1):
            dic1[index] = [i[0]]
        else:
            dic1[index].append(i[0])
    return list(sorted(dic1.items()))
    
def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    dic1 = {}
    for i in listadef:
        current = dic1.get(i[1],-1)
        if(current == -1):
            dic1[i[1]] = [i[0]]
        else:
            dic1[i[1]].append(i[0])
    sort = list(sorted(dic1.items()))
    final = []
    for i in sort:
        final.append((int(i[0]),list(sorted(set(i[1])))))
    return final

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    dic1={}
    for i in listadef:
        for i in i[4].split(","):
            dic1[str(i[:3])] = dic1.get(str(i[:3]),0) + 1
    return dict(sorted(dic1.items()))


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    lista1 = []
    for i in listadef:
        lista1.append((i[0],len(i[3].split(",")),len(i[4].split(","))))
    return lista1


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    dic1={}
    for row in listadef:
        for i in row[3].split(","):
            dic1[str(i)] = dic1.get(str(i),0) + int(row[1])
    return dict(sorted(dic1.items()))


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    dic1={}
    for row in listadef:
        for i in row[4].split(","):
            dic1[row[0]] = dic1.get(row[0],0) + int(i[4:])
    return dict(sorted(dic1.items()))
