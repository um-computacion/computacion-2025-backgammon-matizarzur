## [23-08-2025] V 0.0.0
# Agregado:
Carpetas para las clases
Archivos de test para cada clase
# Cambiado o eliminado:
Se cambio los archivos creados anteriormente a las carpetas de sus respectivas clases para que queden junto a sus archivos de test
cambio en el nombre del archivo de cli: main.py --> cli.py

## [24-08-2025] V 0.0.1
# Agregado:
Archivos y lineas de comandos necesarias para la implementacion de CircleCi

## [25-08-2025] V 0.0.2
# Cambiado: 
Se arreglo la localizacion de los archivos test, se movieron a la carpeta test.
Se añadio la clase color_ficha utilizando enums (enumeraciones), que son un conjunto fijo y definido de constantes con nombres, en este caso se utilizan para el color de la ficha en la clase checker. 

## [25-08-2025] V 0.0.3
Se agrego el archivo .coveragerc y se configuro de acuerdo al proyecto.

## [30-08-2025] V 0.0.4
Se corrigieron los nombres de las clases. Se continuo trabajando sobre la clase Board, se agregaron metodos, verificaciones y setters. Ademas se añadieron test para una mayor covertura de codigo (tambien debido a la creacion de nuevos metodos se añadieron tests).
Se deja el coverage en un 92% comparado al 89% que se tenian antes de los arreglos.

## [30-08-2025] V 0.0.5
Se agrega la clase dice segun lo visto en clase, ademas se agregan algunos metodos para una mejor funcionalidad.
Se crean test para la clase dice.
Se corrigio la clase para utilizar getters y setter, ademas tambien se corrigio la encapsulacion. Tambien se cambio la logica de dobles porque era un poco confusa.

## [11-09-2025] V 0.0.6
Se comenzo con la clase BackGammon Game.Se agregaron atributos principales:board, dice, jugador_actual,estado_juego, ganador, barras de fichas capturadas y tiradas iniciales. Se implementaron getters y setter con validaciones para cada atributo.Se definieron los métodos principales del flujo de juego como placeholders (configuración, tiradas, movimientos, validaciones, cambio de turno, verificación de ganador, etc)
Estructura preparada para avanzar con la lógica del juego en versiones futuras.

## [14-09-2025] V 0.0.7
Se corrige la clase board con un metodo adicional, tambien se agregan test necesarios para una mayor cobertura del codigo. Se elimina lo realizado en la clase Backgammon game porque se retomara despues de haber corregido algunas clases y haber añadido la clase player.
## [14-09-2025] V 0.0.8
Se elimina la carpeta CircleCI debido a que no se trabajara segun lo visto en la clase virtual. 
Se agregan las librerias necesarias
Se añaden los archivos y configuraciones necesarias para su funcionamiento

## [15-09-2025] V 0.0.9
Se cambia el codigo dentro de /.github/workflows/ci.yml para una mejora en el aspecto de los tests, analisis de los directorios, mejor debugging y demas.
## [15-09-2025] V 0.1.0
Se agregan budgets en el README.md para que se muestre la informacion tipica del proyecto.
Se corrigio varias veces el ci.yml para que actulice automaticamente los budges del README

## [16-09-2025] V 0.1.1
Se corrigen y se pulen algunos puntos flojos del codigo para mejorar su valoracion, intentando que no afecte al coverage ni a la logica.
Se agregaron los docstrings solicitados por el ci.yml