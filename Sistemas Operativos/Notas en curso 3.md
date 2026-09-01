Dispositivos entrada salida


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