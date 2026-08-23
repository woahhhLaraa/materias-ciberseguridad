---
materia: Arquitectura de redes
semestre: 2
tipo: proyecto
tags: [redes, diseno, wlan, uv, econex]
---

# Proyecto red ECONEX

Análisis de requerimientos para el rediseño de la red del edificio ECONEX de la Facultad de Estadística e Informática, UV. Corresponde a la **fase 1** de la [[Metodologia de diseno de redes top-down]].

## 1. ¿Qué población se va a atender?

La red diseñada para el edificio ECONEX de la Facultad de Estadística e Informática estará orientada a atender a toda la comunidad universitaria adscrita a la Universidad Veracruzana, bajo el esquema institucional de la Red Inalámbrica Universidad Veracruzana (RIUV).

La población objetivo incluye:

-   Estudiantes activos de la Facultad.
-   Docentes e investigadores.
-   Personal administrativo.
-   Estudiantes y personal académico de otras facultades de la UV que requieran acceso temporal al edificio.
-   Usuarios institucionales debidamente registrados en el sistema de autenticación de la Universidad.

El acceso a la red se realizará mediante autenticación institucional, utilizando las credenciales oficiales (matrícula y contraseña) asignadas a cada miembro de la comunidad UV, a través de un sistema de red cautiva o autenticación centralizada. Esto garantiza que únicamente usuarios autorizados puedan hacer uso de los recursos de red.

## 2. ¿Qué servicios de red requieren los estudiantes de la UV?

Los estudiantes requieren principalmente conectividad confiable, estable y de alto rendimiento tanto inalámbrica como alámbrica.

Los servicios requeridos incluyen:

-   Acceso inalámbrico (WiFi) distribuido estratégicamente mediante Access Points en aulas, pasillos, áreas comunes, biblioteca y zonas de estudio del edificio ECONEX.

-   Acceso cableado mediante puertos Ethernet en laboratorios y salas de cómputo, para:

    -   Equipos de escritorio institucionales.
    -   Dispositivos personales cuando se requiera mayor estabilidad o velocidad.
    -   Prácticas académicas relacionadas con redes y ciberseguridad.

El diseño debe contemplar alta concurrencia en horarios pico, garantizando:

-   Buena capacidad de ancho de banda.
-   Baja latencia.
-   Estabilidad en la autenticación.
-   Balanceo adecuado de carga entre Access Points.

## 3. ¿Qué servicios desea ofrecer la Universidad?

La Universidad Veracruzana, a través de esta infraestructura, busca ofrecer:

-   Conectividad institucional segura (RIUV).
-   Acceso a servicios académicos en línea (plataformas educativas, repositorios digitales, sistemas escolares).
-   Comunicación interna institucional.
-   Acceso a servidores centrales del campus Xalapa.

Posibles servicios adicionales (como propuesta de mejora):

-   Segmentación de red mediante VLAN para separar tráfico de estudiantes, docentes y administrativos.
-   Implementación de red de invitados controlada para eventos académicos.
-   Sistema de monitoreo y gestión centralizada de red.
-   Implementación de políticas de calidad de servicio (QoS) para priorizar tráfico académico sobre tráfico recreativo.
-   Autenticación segura mediante protocolos como WPA3-Enterprise.

## 4. ¿Qué tipos de dispositivos se van a conectar?

La red debe soportar un entorno heterogéneo de dispositivos, entre ellos:

-   Dispositivos móviles (smartphones y tablets).
-   Laptops personales de estudiantes y docentes.
-   Computadoras de escritorio institucionales.
-   Equipos administrativos.
-   Impresoras en red.
-   Dispositivos de oficina con conectividad IP.
-   Equipos de laboratorio relacionados con prácticas académicas.
-   Posibles dispositivos IoT institucionales (cámaras, controles de acceso, etc.).

El diseño deberá contemplar compatibilidad con múltiples sistemas operativos y una alta densidad de dispositivos por usuario.

## 

## 5. ¿Qué otros requerimientos tiene la UV, sus directivos y sus docentes?

Desde el punto de vista institucional y de seguridad, se identifican los siguientes requerimientos:

1.  Integración con la infraestructura central del campus Xalapa.\
    La red del edificio ECONEX debe enlazarse con los servidores principales de la Universidad, posiblemente ubicados en la zona universitaria (Zona UV o Rectoría), mediante un enlace inalámbrico institucional ya existente (antena instalada en el techo del edificio).

2.  Seguridad y segmentación de red.\
    Es indispensable que la red esté segmentada para evitar accesos no autorizados a sistemas críticos.

    -   El tráfico de estudiantes no debe tener acceso directo a bases de datos administrativas ni a sistemas sensibles como calificaciones.
    -   Los sistemas críticos deben estar en segmentos protegidos.
    -   Las modificaciones administrativas deben realizarse desde terminales autorizadas o redes internas específicas.

3.  Control de acceso y trazabilidad.\
    La red debe permitir identificar usuarios autenticados para fines de auditoría y seguridad.

4.  Alta disponibilidad.\
    La red debe mantener operación continua durante el horario académico.

## 6. ¿Cuál es el punto de partida? ¿Existe infraestructura disponible?

Sí existe infraestructura previa.

El diseño no parte desde cero, sino que busca optimizar y reforzar la infraestructura actual de la RIUV dentro del edificio ECONEX.

Debilidades identificadas:

-   Número insuficiente de Access Points.
-   Saturación en horarios pico debido a alta concurrencia.
-   Disminución en velocidad y estabilidad.
-   Dificultades de conexión para usuarios nuevos en momentos de alta demanda.

Por lo tanto, el proyecto se enfoca en:

-   Mejorar cobertura inalámbrica.
-   Incrementar capacidad de atención simultánea.
-   Optimizar distribución y configuración de Access Points.
-   Proponer segmentación y mejoras de seguridad.
-   Mejorar experiencia de autenticación en horas críticas.

## Documentos

- ![[Proyecto red econex.dotx]] — plantilla

## Relacionadas

- [[Metodologia de diseno de redes top-down]] — la fase que este documento cubre
- [[Diseno de red LAN]]
- [[Redes confiables]] — escalabilidad, QoS y seguridad son exactamente los ejes del proyecto
- [[Tendencias de red]] — BYOD explica la necesidad de segmentación por VLAN
