---
materia: Introduccion a las redes de computo
semestre: 2
tipo: caso
tags: [ciberseguridad, ransomware, mexico, infraestructura-critica]
---

# Caso Pemex — ransomware DoppelPaymer

## El incidente

En **noviembre de 2019**, **Petróleos Mexicanos (Pemex)** sufrió uno de los incidentes de ciberseguridad más relevantes en la historia reciente de México. Un ataque de **ransomware** comprometió los sistemas internos de la empresa, bloqueando equipos y servidores críticos. Los atacantes exigieron un rescate equivalente a varios millones de dólares en bitcoins a cambio de la clave de descifrado.

## Impacto

El ataque afectó significativamente las **operaciones administrativas**. Durante varios días se limitaron procesos internos, comunicaciones y el procesamiento de datos corporativos. Aunque la producción y distribución de petróleo no se detuvieron por completo, sí hubo afectaciones operativas que obligaron a activar protocolos de contingencia.

## El malware: DoppelPaymer

Se presume que el ransomware utilizado fue **DoppelPaymer**, identificado por primera vez en 2019 y vinculado al sindicato criminal con nexos en Rusia conocido como **Indrik Spider**.

El grupo se especializó en *"big game hunting"*: ataques dirigidos a grandes organizaciones, infraestructuras críticas, sectores de salud, educación y gobiernos, buscando rescates de alto valor.

### Doble extorsión

Su característica más peligrosa fue la adopción temprana de la **doble extorsión** (*double extortion*): antes de cifrar los sistemas, los atacantes **robaban** información sensible y después amenazaban con publicarla en sitios de filtración si la víctima no pagaba.

Esto aumentaba considerablemente la presión, porque **el respaldo deja de ser suficiente**: restaurar los datos no evita su publicación.

## Atribución

Aunque se cree que DoppelPaymer se originó en Indrik Spider, también fue usado por otros grupos con distintos grados de conexión. En el cibercrimen moderno es común que el malware se comparta, alquile o distribuya bajo modelos de **Ransomware-as-a-Service (RaaS)**.

En el caso específico de Pemex **no se identificó oficialmente a un grupo responsable de manera concluyente**. Diversos análisis de inteligencia apuntaron a **TA505**, organización criminal activa desde al menos 2014, conocida por campañas de phishing masivo, distribución de malware bancario y, posteriormente, operaciones de ransomware. TA505 no se ha disuelto y ha estado vinculado a múltiples ataques internacionales posteriores.

## Lecciones

Aunque Pemex declaró que el impacto financiero directo fue mínimo, el incidente evidenció vulnerabilidades importantes en la protección de infraestructuras críticas en México. Puso de manifiesto la necesidad de:

- Fortalecer la ciberseguridad en empresas estratégicas del Estado
- Mejorar la **segmentación de redes**
- Implementar **respaldos robustos**
- Contar con **protocolos formales de respuesta ante incidentes**

El caso se convirtió en punto de referencia en el país para discutir la seguridad digital en el sector energético.

## Esquemas del ransomware

![[ransomware-esquema-1.png]]

![[ransomware-esquema-2.png]]

## Relacionadas

- [[Amenazas y soluciones de seguridad en red]] — el ransomware como amenaza externa, y las capas de solución que le habrían hecho frente
- [[Tipos de atacantes]] — dónde caen Indrik Spider y TA505: crimen organizado con motivación económica
- [[Gestion de incidentes y reportes]] — el marco formal para responder a algo así
- [[Organismos reguladores en Mexico]] — el CERT-MX es quien atiende estos casos
- [[Guerra de los mundos - analisis de ciberseguridad]] — el mismo análisis sobre ficción
