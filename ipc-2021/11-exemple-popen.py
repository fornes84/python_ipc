# /usr/bin/python3
#-*- coding: utf-8-*-
#
# exemple-popen.py ruta
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys, argparse
from subprocess import Popen, PIPE

parser = argparse.ArgumentParser(description=\
        """Exemple popen""")

parser.add_argument("ruta",type=str,\
        help="directori a llistar")

args=parser.parse_args()
# -------------------------------------------------------
command = ["ls", args.ruta]     # Depositem en forma de tupla un primer argument q serà 'ls', i un segon, qserà la ruta
#command = ["who"]
pipeData = Popen(command, stdout=PIPE)      # Crea un tub (popen --> permet construir pipes (constructor)), a l'altre extrem, executa 'ls' de l'argument que li hem passat, 'stdout=PIPE' vol dir que 'stdout' del command, ha d'enviar-ho al tub (pipe)

for line in pipeData.stdout:    # Llegeix cada línea dins del stdout del 'pipe' i la printa
    print(line.decode("utf-8"), end="")
# si no posesim decode no intepretaria els salts de linea i quedarien totes les lineas en série, tamé posaria 'b davant cada linea
exit(0)
