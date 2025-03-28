Cliente y Servidor TCP en Python

Este proyecto implementa un cliente y un servidor TCP en Python que pueden comunicarse en la misma máquina (localhost) usando el puerto 5000. El proyecto incluye dos archivos principales server.py que contiene toda la logica del servidor y client.py que contine toda la logica del cliente

Instrucciones

Requisitos

- Python 3.x instalado
- Libreria socket que viene por defecto con python

Ejecutar el Servidor


Para iniciar el servidor, ejecuta el siguiente comando en consola en la carpeta donde se encuentra el archivo:
```
python server.py
```
El servidor esperará conexiones de clientes.
Para cerrar el servidor, envía el mensaje "TERMINAR SERVIDOR" desde un cliente.

Ejecutar el Cliente

Para iniciar el cliente, usa  en consola en la carpeta donde se encuentra el archivo:
```
python client.py
```
El cliente pedirá al usuario que ingrese un mensaje y lo enviará al servidor esto solo sucedera si existe un servidor disponible al momento de iniciar el programa de cliente de lo contrario recibira un mensaje de error.

Pruebas Manuales
1. **Prueba de mensaje normal:**
   - Ingresa un mensaje cualquiera (ej. "hola").
   - El servidor responderá con el mensaje en mayúsculas.

2. **Prueba de desconexión:**
   - Ingresa "DESCONEXION".
   - El cliente y el servidor cerrarán la conexión correctamente.

3. **Prueba de cierre del servidor:**
   - Ingresa "TERMINAR SERVIDOR".
   - El servidor cerrará todas las conexiones y finalizará su ejecución.

