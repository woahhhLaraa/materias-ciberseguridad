Un usuario es una entidad que interactua con el sistema, bien puede ser o no humano.

Un usuario tiene
- Un nombre de usuario
- En algunos casos puede tener o no contrasena
- Permisos
- Pertenencia a grupos
- Funciones
- Un nimero identificador unico (UID en unix)


Ahora, los usuarios pueden ser servicios, si bien no funcionan como lo haria un humano, donde se tiene el control de la computadora de una forma mucho mas amplia , se llega a esa convencion para aislar permisos. Asi cada servicio tiene ciertos permisos de los que no puede salir, de esa forma, si un servicio se llegase a vulnerar, un atacante solamente podria hacer lo que el usuario de ese permiso puede hacer.
En las primeras versiones de unix, muchos de los servicios corrian como root, obviamente peligroso.

Esto es un patron en todos los sistemas operativos con multiusuario, macos, windows, linux. Pues es la forma de manejar los permisos de un servicio sin tener que inventar nada nuevo, se usa el mismo sistema que se usuaria en un humano.

Por que?
El kernel, para poder manejar los permisos necesita identificar quien quiere hacer cierta accion, solo puede hacerlo si esa entidad tiene una identidad, les damos identidad dandoles un usuario