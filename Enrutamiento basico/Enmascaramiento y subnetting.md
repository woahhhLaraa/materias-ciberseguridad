---
materia: Enrutamiento basico
semestre: 3
tipo: concepto
tags: [redes, ip, mascaras, subnetting]
---

# Enmascaramiento y subnetting

## Enmascaramiento

Quitar información específica de un dispositivo dentro de una IP. En este caso, para **no decirle a un enrutador a qué dispositivo exacto va un paquete** —lo que aumentaría enormemente la dificultad y la complejidad— y que solo le interese **a qué red va**. Dentro de la propia red se define el dispositivo.

Las máscaras y cómo se aplican dependerán del **número de subredes** que una red necesite.

### Ejemplo de cálculo

Si necesitamos **40 subredes**:

```
40 → en binario = 101000 → 6 bits
```

Se toman prestados **6 bits** de la porción de host para identificar la subred.

> Regla general: con *n* bits prestados se obtienen 2ⁿ subredes. Con 6 bits: 2⁶ = 64 ≥ 40 ✓ (con 5 bits solo habría 32, insuficiente).

## Subnetting

Dividir una red en dos o más redes más pequeñas.

### El problema del subnetting clásico

Con el subnetting de la época, **todas las subredes tenían el mismo tamaño**, lo que lleva a ineficiencia en la asignación de direcciones: una subred que necesita 5 hosts recibe el mismo bloque que una que necesita 200.

La solución fue permitir máscaras variables, introduciendo la técnica **VLSM**. Ver [[CIDR y VLSM]].

## Relacionadas

- [[Direccionamiento IP con clases]] — las clases A, B y C de cuya porción de host se toman los bits prestados
- [[Conversion entre bases]] — el binario necesario para calcular máscaras
