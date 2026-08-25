---
materia: Organizacion de computadoras
semestre: 1
tipo: concepto
tags: [hardware, almacenamiento, raid]
---

# Arreglos de discos RAID

Permiten combinar varios discos para almacenar datos. Existen varios niveles; los más comunes en el curso:

| Nivel | Nombre | Cómo funciona | Tolerancia a fallas |
|---|---|---|---|
| **RAID 0** | Conjunto dividido / fragmentación | Reparte la información entre los discos | **Ninguna** |
| **RAID 1** | Conjunto espejo | Crea una copia exacta de los datos en dos o más discos (redundancia) | **Máxima** |
| **RAID 5** | Dividido con paridad | Como RAID 0, pero añade bloques de paridad para verificar errores | Sobrevive a **un** disco caído |

## RAID 5 en detalle

Reparte los datos como RAID 0 pero usa un mecanismo de paridad para revisar errores de transmisión de bytes. Si un disco falla, **los datos se reconstruyen a partir de los bloques de paridad de los otros discos**.

⚠️ Si falla un **segundo** disco antes de reconstruir, se pierden los datos.

## Cómo elegir

- RAID 0 busca **velocidad y capacidad**, sacrificando toda la seguridad
- RAID 1 busca **seguridad**, sacrificando la mitad de la capacidad
- RAID 5 es el compromiso: seguridad razonable con menos desperdicio de espacio

## Relacionadas

- [[Jerarquia de memoria]] — el disco como último escalón de la jerarquía, el que sostiene la memoria virtual
- [[Triada CIA]] — RAID es una medida de **disponibilidad**, no de confidencialidad. Un RAID no es un respaldo.
