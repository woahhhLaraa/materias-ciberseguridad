---
materia: Marco legal y etico de la ciberseguridad
semestre: 2
tipo: concepto
tags: [normativa, cis, pci-dss]
---

# Controles CIS y PCI DSS

## Controles CIS

Conjunto de mejores prácticas para reducir el riesgo de ataques cibernéticos, publicado por el Center for Internet Security.

La distinción importante frente a una **norma**: aquí no hablamos de norma sino de **control**. La diferencia es el grado de libertad —

> Una **norma** da un abanico amplio y los detalles los escoges tú.
> Un **control** da pasos muy específicos de cómo mantener la seguridad.

En su versión 8, los controles relevantes para seguridad física incluyen inventario de activos y etiquetado y control de hardware. Ver [[Normas de seguridad fisica]].

## PCI DSS

**Payment Card Industry Data Security Standard.** Normativa internacional que establece estándares de seguridad para las empresas que manejan datos de tarjetas de pago.

Su objetivo es proteger los datos de los titulares de las tarjetas y prevenir incidentes de seguridad. Es la normativa más importante a nivel mundial en el sector financiero.

## Cuándo aplica cada marco

| Contexto | Marco |
|---|---|
| Datos personales de clientes | GDPR / [[LFPDPPP - Ley de proteccion de datos]] |
| Sector financiero y tarjetas | PCI DSS |
| Gestión general de la información | [[ISO-IEC 27001]] |
| Gestión de riesgo (sector privado, EE. UU.) | [[NIST CSF]] |
| Pasos técnicos concretos | Controles CIS |

## Relacionadas

- [[Estandares de seguridad]] — el panorama general de marcos donde estos dos encajan
- [[ISO-IEC 27001]] — la norma certificable frente a la que se define el contraste norma/control
- [[Familia ISO 27000]] — la 27002 tambien lista controles, pero mas abiertos que los del CIS
- [[NIST CSF]] — el otro marco estadounidense de gestion de riesgo, mas flexible que PCI DSS
- [[Normas de seguridad fisica]] — los controles CIS v8 de inventario y etiquetado de hardware aterrizan ahi
- [[Marco legal y etico de la ciberseguridad]] — indice de la materia
