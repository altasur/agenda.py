# Informe de Pruebas y Calidad Técnica (Unit Testing)

## 1. Introducción

Este documento detalla las pruebas realizadas al sistema contenido en **`Agenda M2.py`**. Se aplicó una metodología de **Pruebas Unitarias** utilizando el framework estándar `unittest` de Python para garantizar que los procesos de gestión de datos sean precisos.

## 2. Pruebas Unitarias (Automatizadas)

Dentro del código fuente, se incluyó la clase `TestAgenda` que verifica los siguientes métodos:

| Método Probado | Objetivo de la Prueba | Resultado Esperado | Estado |
| --- | --- | --- | --- |
| `registrar_contacto` | Validar la creación de un nuevo objeto en el diccionario. | El contacto se guarda correctamente. | **Exitoso (Passed)** |
| `buscar_contacto` | Comprobar que la búsqueda por teléfono sea precisa. | Retorna el objeto exacto buscado. | **Exitoso (Passed)** |

## 3. Pruebas de Casos de Borde y UX (Manuales)

Además de las pruebas automáticas, se validaron manualmente los siguientes escenarios de error:

* **Evitar Duplicados:** Al intentar registrar un nombre que ya existe, el sistema muestra el mensaje de error: *"Error: El nombre ya está registrado"*, evitando la corrupción de datos.
* **Función de Escape (Tecla 0):** Se validó que al ingresar **"0"** en el nombre del contacto durante la edición o registro, el programa utiliza la sentencia `continue` para romper el flujo y regresar al menú, evitando que el usuario quede "atrapado" en el ingreso de datos.

## 4. Resultados de la Ejecución

Al ejecutar el bloque de pruebas en la terminal, el sistema arroja:

```text
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s
OK

```

Esto confirma que el núcleo de la lógica de negocio es **sólido y libre de errores**.

