# TareaBuda
Tarea de test técnico para postulación trabajo de Buda

## Descripción de red
En la carpeta `Examples` podemos encontrar el archivo `red1.txt`que representa la red del enunciado.

Este archivo contiene en la primera linea los nombres a utilizar para cada estación separados por un espacio en blanco.
Desde la segunda linea en adelante se describe una matriz cuadrada de **NxN** donde N es la cantidad de estaciones de la red descrita. Cada fila y columna representa una estación, estas siguen el mismo orden de las estaciones de la primera linea del archivo, por ejemplo, la tercera columna de la matriz representa la tercera estación de la primera linea del archivo.   
Para cada par de estaciones **(ixj)** de dicha matriz, donde **i** es distinto de **j**, se asigna un 0 si no existe conexión entre dichas estaciones y un 1 si existe conexión. La matriz es simétrica ya que en la red de metro las conexiones no son dirigidas.
En la diagonal de la matriz para cada **(ixi)** tiene un 0 si la estación **i** es blanca, un 1 si es roja y un 2 si es verde.

## Utilizar programa

Para utilizar el programa se debe ejecutar bajo el siguiente formato:
~~~
python main.py [path_archivo_red] [nombre_estación_inicial] [nombre_estación_final] [color_vagon]
~~~
* `[path_archivo_red]`: Es la ruta del archivo que describe la red.
* `[nombre_estación_inicial]`: Nombre de la estación de partida. 
* `[nombre_estación_final]`: Nombre de la estación de llegada.
* `[color_vagon]`: Es el único parámetro **opcional**, los colores que se pueden ingresar para el vagon son *white*, *red* y *green*. Si no se ingresa nada se asume que el color del vagon es *white*

Ejemplos de posibles ejecuciones son:
~~~
python main.py Examples\red1.txt I B green
python main.py Examples\red1.txt A F
python main.py Examples\red1.txt A H red
~~~

## Resultado

Para cada ejecución del programa se imprime la menor ruta entre las estaciones analizadas separadas por `->` indicando la dirección pedida. Para los ejemplos de las posibles ejecuciones se tiene los siguientes resultados:
~~~
I->G->C->B
A->B->C->D->E->F
A->B->C->H
~~~
