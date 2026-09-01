Dispositivos entrada salida

Como se comunica un controlador con la CPU

El controlador o driver es una tarjeta dentro del dispositivo de entrada o salida
El controlador o driver conecta a la cpu y al dispositivo mediante los componentes de memoria internos del propio chip del controlador

- Registros de E/S: para hacer lectura y escritura
	- Registro de datos: El cpu aqui puede escribir o leer datos en el controlador
	- Registro de estado: Aqui el cpu lee como se encuentra el dispositivo, encendido, apagado, error.
	- Registro de control: Aqui el cpu le indica que hacer al dispositivo, lee, escribe, enciende el motor
		- El cpu usa el registro de control (comandos) para poder leer o escribir dentro del registro de datos.
		- Se usan todos al mismo tiempo para hacer una operacion, no es que se use uno y luego otro
- Puertos o direcciones de entrada salida:
	- Sirven como puente para la conexion entre el CPU y el dispositivo E/S.
	- Dan un nombre especifico y unico a todos los registros que tengan que ver con el dispositivo.
	- Definen el metodo de acceso que utilizara el procesador para leer o escribir datos. (memoria compartida, o sin memoria compartida[[Tecnicas de entrada y salida]] )



Paralelismo:


Concurrencia: Existencia de mas de una tarea progresando de manera de simultanea en el tiempo

Ofrecne continuidad operativa: No se congela al realizar mas de una tarea
Optimizacion de recursos: El cpu no se queda inactivo nunca
Automatizacion fluida: Las actualizaciones del sistema o copias de seguridad ocurren sin detener el trabajo diario



Consideraciones para instalar un SO
Requerimientos de hardware
Firmware de placa
Backup
Tipo de licencia
Esquema de tabla de particiones
Sistema de archivos
Estrategia de particionado
- MBR
- GPT
Sistemas de archivos
- NTFS
- ext4/BTRFS
- APFS
Estrategia de particionado
- Root
- Home
- Swap
Tipos de instalacion
- Limpia
- Actualizacoin
- Arranque múltiple
Metodos de despliegue
- Usb ejecutable
- Por red
Actualizaciones criticas
Controladores
Hardening



Investigar diferencia BIOS y UEFI



reporte creacion de maquina virtual todo lo que hice paso a paso
1. Instale virtualBox en debian
2. Configuracion de la maquina virtual
	1. Ponerle un nombre
	2. Donde la voy a almacenar
	3. Que imagen voy a usar (no lo seleccione, no la hice desatendida)
	4. le di 2gb de memoria ram
	5. le di 2 cpus
	6. le di 50 gb de disco
	7. ![[Pasted image 20260831093935.png]]
	8. hard disk type vdi por defecto
	9. modo experto
	10. ![[Pasted image 20260831094852.png]]
	11. Conecte la computadora al ethernet de la RIUV
	12. fui a almacenamiento![[Pasted image 20260831095132.png]]
	13. seleccione la imagen ISO
	14. inicie la maquina
	15. graphical install
	16. espanol
	17. ubicacion mexico
	18. continuar
	19. escogi el nombre de la maquina (pc-jazzMan)
	20. nombre de dominio en blanco
	21. configure los usuarios y contraseñas (superusuario[jazzist], usuario[30041945])
		1. Se reocmienda una contraseña diferente dependiendo de si es usuario o superusuario
	22. Nombre completo para el nuevo usuario Pedro Lara
	23. Nombre del usuario Larita
	24. Reloj zona central
	25. Particionado de discos en tres (manual)
		1. /root 25 gb
			1. Primaria
			2. Al principio
			3. Utilizar como ext4
			4. Punto de montaje /
		2. home 21 gb
			1. Logica (investigar diferencia entre primaria y logica)
			2. Al principio
		3. swap 4 gb (memoria virtual para darle soporte al sistema operativo)
			1. Logica
			2. Area de intercambio
			3. Al principio
	26. Finalizar el particionado y escribir cambios en el disco
	27. Replica de red de debian en mexico
	28. Sin entorno de escritorio
	29. utilidades estandar del sistema y ssh
	30. SI cargar GRUB




Investigar particiones en linux