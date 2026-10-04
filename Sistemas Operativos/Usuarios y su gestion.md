Que es un usuario?
Es una entidad que interactua con el sistema operativo o es el destino de uno de sus servicios ya sea publico, privado, empresarial o profesional, puede ser un humano o no. "Aquel que hace algo"

Que hace un usuario?
Un usuario (humano) administra sus propios archivos
Un usuario (humano o no) da ordenes al sistema para que realice acciones especificas o procesos especificos.
Dependiendo de si ese usuario es administrador (superusuario) o no, puede administrar otros usuarios, o procesos.

Los usuarios normalmente tienen un nombre de usuario, y dado el caso, una contrasena. Ademas, en el caso de sistemas tienen un numero unico de usuario UID (user identifier) y un identificador de su grupo GID (group identifier)

Tipos de usuario:
Administradores o superusuario: Los usuarios con mayor poder en el sistema operativo, en linux se le conoce como root.

Usuario estandar: El usuario con el que se inicia sesion dentro del sistema, con permisos mas limitades a comparacion del root. Este tiene su propio espacio de trabajo /home/nombre_del_usuario

Usuario invitado: Un usuario estandar, con menos privilegios, solamente para accesos temporales, sin la posibilidad de cambiar configuraciones avanzadas, quitar o instalar algo.

Usuario especial: Es lo que llamamos "Un usuario no humano", muy ligado a los daemon, generalmente con una UID entre 1 y 100, estos usuarios no tienen contrasena, son basicamente procesos con permisos. A los procesos se les da un usuario para poder llevar sus permisos.