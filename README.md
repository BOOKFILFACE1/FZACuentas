# FZACuentas

El brute-force o ataque de fuerza bruta es un procedimiento de hackeo mediante el cual se busca adivinar una contraseña, probando aleatoriamente combinaciones de caracteres tomando en cuenta algunos aspectos de la víctima.
El programa trabaja con un algoritmo simple, que irá probando distintas contraseñas hasta que logre adivinar la correcta.

Para facilitar el funcionamiento del ataque de fuerza bruta, se recomienda el uso del método Diccionario.

A través de este, se proporciona un archivo .txt con una lista de contraseñas que posiblemente puede contener la correcta.

Para definir cuál sería la posible contraseña, se trabaja con un conjunto de factores que definen su validez.

Teniendo en cuenta este detalle, se debe iniciar el proceso de clonación del programa de ataque, utilizando este comando:

git clone https://github.com/BOOKFILFACE1/FTACuentas.git.

Se iniciará el proceso de clonación que permitirá guardar el programa en tu computadora.

El comando que se muestra a continuación permitirá gestionar los permisos del programa e ingresar el directorio donde se encuentra:

chmod -R 755 FTACuentas && cd FTACuentas

Aquí observaremos dos archivos. Uno bajo el nombre de README.md y el otro como instagram.py. Ejecutaremos este último:

python3 FTACuentas.py

Nos lanzará un error, ya que será necesario disponer de un archivo .txt que permitirá el ataque de fuerza bruta con diccionario.
