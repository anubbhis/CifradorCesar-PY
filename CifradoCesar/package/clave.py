import os
def clave():
	clave = 0
	while True:
		clave = int(input("\nseleccione la clave de encriptado desplazada entre 1-26 \n" + '\n'))
		if clave >=1 and clave<=26:
			return clave