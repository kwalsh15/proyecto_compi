def cargar(ruta):

    with open(ruta) as archivo:
        for i in archivo:
            yield i.strip("\n")