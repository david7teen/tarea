# 1. Nombre y explique brevemente los pilares de la POO.
#abstracción:mostrar solo lo mas relevante y omitir detalles que nos nos interesen. encapsulamiento:definir quien puede interactuar y modificar los objetos de nuestra clase.
#herencia:los atributos que "heredan" las clases hijos que estan por debajo de la clase madre. polimorfismo:es cuando heredamos cierto atributo, independiente de la clase.


#2. Explique y ejemplifique el concepto de clase.
#una clase es donde se guardan y clasifican los objetos que se desean crear, ej: una clase auto, puede tener modelos de autos o tener un mismo modelo y clasificarlos por su color, tamaño, caballos de fuerza, etc.

#3. Explique y ejemplifique el concepto de objeto. 
#un objetos es aquel entidad que tiene atrbutos o metodos, ej: un auto de atributo tiene color, tamaño, numero de asientos, y los metodos serian cuantos litros de gasolina/petroleo/diesel ocupa en ciertos kilometros, o en cuantos segundos se demora en llegar a los 100km/h.

from Trabajador import Trabajador
from encuesta import encuesta

m1=Trabajador("fem","pedro",23,1,24)
m2=Trabajador("masc","lola",23,2,33)
m3=Trabajador("masc","lolo",23,3,33)

ola=encuesta([m1,m2,m3])
ola.Menu()