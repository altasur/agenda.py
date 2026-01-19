# Documentación Técnica: Sistema de Gestión de Contactos V2.1

## 1. Arquitectura del Proyecto

El sistema se ha diseñado siguiendo el paradigma de **Programación Orientada a Objetos (POO)** para garantizar la modularidad y el correcto tratamiento de los datos. La lógica se divide en:

* **Clase `Contacto**`: Representa la entidad del cliente, encapsulando los atributos: nombre, teléfono, email y dirección.
* **Clase `Agenda**`: Actúa como el motor del sistema. Utiliza una estructura de **Diccionario** para almacenar los objetos. Como analista de datos, seleccioné esta estructura para asegurar que la búsqueda por nombre sea inmediata (eficiencia ), facilitando la escalabilidad del sistema.

## 2. Módulos Utilizados

* **`Agenda M2.py`**: Archivo principal que contiene tanto las clases de lógica como la interfaz de usuario y el módulo de pruebas.
* **`unittest`**: Librería estándar de Python integrada para realizar pruebas automatizadas y asegurar la calidad técnica del registro y búsqueda.

## 3. Instrucciones de Ejecución

Para correr la aplicación en un entorno local:

1. Asegúrese de tener instalado **Python 3.x**.
2. Descargue el archivo **`Agenda M2.py`** de este repositorio.
3. Abra una terminal en la carpeta donde guardó el archivo.
4. Ejecute el siguiente comando (use comillas debido al espacio en el nombre):

bash:
python "Agenda M2.py"

## 4. Guía de Uso y Navegación

La interfaz es intuitiva y se opera mediante la consola:

* **Navegación**: Seleccione una opción del 1 al 6.
* **Opción de Escape (Tecla 0)**: En los submenús de Registro, Búsqueda, Edición o Eliminación, puede ingresar el número **`0`** para cancelar la acción y regresar inmediatamente al menú principal.
* **Edición Selectiva**: Al editar, si deja un campo vacío y presiona `Enter`, el sistema conservará el dato original del contacto.

## 5. Documentación Interna (Docstrings)

El código en **`Agenda M2.py`** cuenta con comentarios explicativos y **Docstrings** bajo el estándar PEP 257. Cada método describe su funcionalidad, lo que garantiza que el proyecto sea comprensible y fácil de mantener.
