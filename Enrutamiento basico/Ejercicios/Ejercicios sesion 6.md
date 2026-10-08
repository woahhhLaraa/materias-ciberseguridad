---
materia: Enrutamiento basico
tipo: ejercicios
sesion: 6
---

# Ejercicios sesión 6 — Calentamiento: rutas estáticas

Parte del «Recuperar» de la sesión 6 en [[Temario primer parcial]]. Sin apuntes, 10–15 min. Lo que falles, al registro de fallos.

## Enunciado

R1 se conecta a R2 por el enlace **10.0.0.0/30** (R1 = .1, R2 = .2). Detrás de R2 están las redes:

- 172.16.8.0/24
- 172.16.9.0/24
- 172.16.10.0/24
- 172.16.11.0/24

a) Ruta estática en R1 solo hacia 172.16.9.0/24.
b) Ruta por defecto en R1 hacia R2.
c) Una sola ruta sumarizada en R1 que cubra las cuatro redes. Indica la red, el prefijo y la máscara en decimal.

## Soluciones

> [!success]- Ver soluciones (no abrir hasta terminar)
> a) `ip route 172.16.9.0 255.255.255.0 10.0.0.2`
>
> b) `ip route 0.0.0.0 0.0.0.0 10.0.0.2`
>
> c) Tercer octeto en binario: 8 = 000010**00**, 9 = 000010**01**, 10 = 000010**10**, 11 = 000010**11**. Comparten los 6 primeros bits → 16 + 6 = **/22**.
> Red resumen **172.16.8.0/22**, máscara **255.255.252.0** (8 es múltiplo de 4, así que el bloque es válido).
> `ip route 172.16.8.0 255.255.252.0 10.0.0.2`
