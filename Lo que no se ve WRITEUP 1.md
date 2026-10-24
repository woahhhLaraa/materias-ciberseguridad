Esteganografía
400 puntos

Me dieron un .zip que dentro contenia un archivo txt

Lo primer que hice fue descomprimir el .zip
Correr file nombresdelosarchivos en cada uno
confirmando que tanto el zip como el txt son lo que dicen ser

Leyendo el texto entero me encuentro con el siguiente pasaje:
"La única manera de saberlo es dejar de leer como lector y empezar a leer como máquina,
byte por byte, hasta que el mensaje decida mostrarse a quien tuvo la paciencia de buscar."

Mi hipotesis: Hay texto escondido, invisible

La unica forma que se me ocurrio de esconder texto plano es mediante caracteres que no se ven.

comando: cat -A

Me mostro que hay "espacios dobles" probablemente algun UTF extraño.

Necesito reemplazar todos los espacio raros por algo visible
Abri CyberCHEF, para reemplazar texto
No me ayudo, hay un mensaje en los textos que no puedo reemplazar

Investigue en internet problemas parecidos en foros.

Los mas probable: Los espacios raros son 0, los espacios normales son 1.

Luego tuve que borrar los caracteres normales para que no estorben

Quedé con una secuencia en binario, la traduzco ahi mismo en cyberCHEF

Quede con un string? pero esa no es la flag
El string es un hexdump
Uso cyberchef para traducir hexdump

Me dio la flag, la subi y la acepto.