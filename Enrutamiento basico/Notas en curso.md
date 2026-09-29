---
materia: Enrutamiento basico
semestre: 3
tipo: captura
tags: [captura, sin-procesar]
---
# Enrutamiento basico — notas en curso

17 de septiembre
Distancia administrativa
Es mas un concepto de jerarquizacion que una tecnica
Cuando usamos enrutamiento dinamico cada protocolo tiene una distancia administrativa dinamica, por defualt la distancia empezando por las estaticas es la distancia 1
Un valor de 8 bits 0-255 que me permitira de manera arbitraria cual es el camino las "idoneo"
El enrutador siempre tratara de ir por la menor distancia administrativa
La distancia adminstrativa esta por encima de los protocolos
si la distancia administrativa se ve comprometida, el router escoge una ruta mediante una metrica

Un ejemplo de jerarquizacion con distancia administrativa
Directamente conectada : 0 (la mas confiable y preferida)
Ruta estatica : 1 (generalmente muy confiable)
OSPF : 110(protocolo dinamico confiable)
RIP : 120 (menos confiable que OSPF)
Desconocida o invalida: 255 (se descarta automagicamente)

Protocolo de distancia de primer salto
Si falla el router de puerta de salida, los host configurados quedan aislados, se necesita un mecanismo de alternativas de salida en redes donde hay mas de dos routers a la misma red local o virtual. De manera normal no deberiamos tener dos puertos o dos routers conectados a la misma red, 

FIRST HOP REDUDANT PROTOCOL FHRP
dar mayor seguridad siempre teniendo un segundo enrutador, basados en la idea de las ips virtuales y macs virtuales                                                        

La redundancia de routers

a dos routers con su ip les damos aparte una ip virtual y esos dos routers se ponen dea acuerdo para funcionar o no segun si el otro funciona o no, a las pcs se les de el default getaway con ip dirigida a la direccio nvirutal de los router. a los ojos de los hosts, siempre mandan paquetes a la misma ip


reenvio de paquetes:
proceso de decision despues de que el router decidio cual es la mejor ruta, debe determinar como encapsular el parquete, reenviarlo hacia fuera la interfaz de salida correcta

24 septiembre





> Índice de la materia: [[Enrutamiento basico (materia)]]

