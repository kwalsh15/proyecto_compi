#Archivo Principal
from utils import archivos as utils
from explorador.explorador import Explorador

import argparse

parser = argparse.ArgumentParser(description='Interprete para Ewa Kaska')

parser.add_argument('-explorar', dest='explorador', action='store_true',
        help='Explorar')

parser.add_argument('archivo',
        help='Archivo de código fuente')

def ewaKaska():

    args = parser.parse_args()

    if args.explorador is True: 

        texto = utils.cargar(args.archivo)

        exp = Explorador(texto)
        exp.explorar()
        exp.printElementos()
        exp.imprimirPalabrasInvalidas()

    elif args.python is True:

        texto = utils.cargar(args.archivo)

        exp = Explorador(texto)
        exp.explorar()


    else:
        parser.print_help()


if __name__ == '__main__':
    ewaKaska()
