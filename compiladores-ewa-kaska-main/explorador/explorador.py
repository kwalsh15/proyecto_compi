from enum import Enum, auto

import re

#Esta clase contiene los enum para manejar los diferentes tipos de elementos del lenguaje
class Elemento(Enum):
    comentario = auto()
    palabraClave = auto()
    condicional = auto()
    repeticion = auto()
    asignacion = auto()
    operador = auto()
    comparador = auto()
    texto = auto()
    identificador = auto()
    entero = auto()
    flotante = auto()
    booleano = auto()
    puntuacion = auto()
    blancos = auto()
    ninguno = auto()
    funcion = auto()
    cuerpo = auto()
    recorrer = auto()
    devolver = auto()


class Lexico:
    tipo    : Elemento
    texto   : str

    def __init__(self, tipoNuevo: Elemento, textoNuevo: str):
        self.tipo = tipoNuevo
        self.texto = textoNuevo

    def __str__(self):
        resultado = f'{self.tipo:30} <{self.texto}>'
        return resultado

class Explorador:

    Elementos  = [(Elemento.comentario, r'^\bchok:\b'),
                               (Elemento.condicional, r'^(\beta\b)'),
                               (Elemento.repeticion, r'^(\bamauk\b)'),
                               (Elemento.asignacion, r'^(\bdor\b)'),
                               (Elemento.funcion, r'^(\bdel\b)'),
                               (Elemento.cuerpo, r'^(\bkewe\b|\bbata\b)'),
                               (Elemento.devolver, r'^(\bdokmale\b)'),
                               (Elemento.recorrer, r'^(\bie\b|\be\b)'),
                               (Elemento.operador, r'^(\bukotkok\b|\bshok\b|\bbalatok\b|\bberie\b)'),
                               (Elemento.comparador, r'^(\btse\b|\bkibi\b|\bbtaie\b|\bkuoki\b)'),
                               (Elemento.texto, r'^(~.?[^~])~'),
                               (Elemento.identificador, r'^([a-z][a-zA-Z0-9_]+)'),
                                (Elemento.entero, r'^(-?[0-9]+)'),
                               (Elemento.flotante, r'^(-?[0-9]+.[0-9]+)'),
                               (Elemento.booleano, r'^(\bchokale\b|\bkocho\b)'),
                                (Elemento.puntuacion, r'^([,{}()])'),
                                (Elemento.blancos, r'^(\s)')]

    # Constructor de la clase
    def __init__(self, contenido_archivo):
        self.texto = contenido_archivo
        self.elementos = []
        self.palabras_invalidas= set()

    # Recorre todas las palabras del archivo de texto
    def explorar(self):
        for i in self.texto:
            resultado = self.procesar(i)
            self.elementos = self.elementos + resultado

    # Imprime los elementos
    def printElementos(self):
        for i in self.elementos:
            print(i)

    def imprimirPalabrasInvalidas(self):
        if len(self.palabras_invalidas) > 0:
            print("Las siguientes palabras no pertenencen al lenguaje:")
            for palabra in self.palabras_invalidas:
                print(palabra)
        else:
            print("No se encontraron palabras erroneas")

    # Recorre el txt buscando los elementos lexicos
    def procesar(self, linea):

        elementos = []
        es_palabra_valida = False
        # Toma una línea y le va cortando pedazos hasta que se acaba

        # Separa los descriptores de componente en dos variables
        palabras = linea.split()
        for palabra in palabras:
            for tipoElemento, regex in self.Elementos:

                # Trata de hacer match con el descriptor actual
                respuesta = re.match(regex, palabra)

                # Si hay coincidencia se procede a generar el componente
                # léxico final
                if respuesta is not None:
                    # si la coincidencia corresponde a un BLANCO o un
                    # COMENTARIO se ignora por que no se ocupa
                    if tipoElemento is not Elemento.blancos and \
                            tipoElemento is not Elemento.comentario:
                        # Crea el léxico y lo guarda
                        nuevoElemento = Lexico(tipoElemento, respuesta.group())
                        if(str(nuevoElemento.tipo) == "Elemento.identificador") and len(re.findall(r'tse|dokmale|del', linea)) == 0:
                            es_palabra_valida = False
                        else:
                            elementos.append(nuevoElemento)
                            es_palabra_valida = True
                        linea = linea[respuesta.end():]
                        break
            if not es_palabra_valida:
                self.palabras_invalidas.add(palabra)
            es_palabra_valida = False
            break

        return elementos