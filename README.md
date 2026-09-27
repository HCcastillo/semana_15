# Restaurante App – Semana 15

## Datos del estudiante

**Nombre:** Hugo Carlin Castillo Calva
**Materia:** Programación Orientada a Objetos
**Semana:** 15
**Proyecto:** Restaurante App

---

## Descripción del proyecto

El proyecto **Restaurante App** es una aplicación desarrollada en Python utilizando el paradigma de **Programación Orientada a Objetos (POO)**. La aplicación permite gestionar información de productos, usuarios y ventas mediante una interfaz gráfica.

Para esta semana se continúa trabajando sobre la estructura desarrollada en las semanas anteriores, manteniendo la separación entre modelos, servicios, interfaz gráfica y archivos de datos.

La información de la aplicación se almacena en archivos **JSON**, permitiendo conservar los datos aunque el programa se cierre y vuelva a ejecutarse.

---

## Objetivo

Continuar el desarrollo de la aplicación Restaurante App aplicando conceptos de Programación Orientada a Objetos, separación de responsabilidades, componentes de interfaz gráfica y persistencia de información.

También se busca mantener una estructura organizada que permita agregar nuevas operaciones sin tener que reconstruir todo el proyecto.

---

## Funcionalidades

La aplicación cuenta con las siguientes funcionalidades principales:

* Inicio de sesión mediante usuario y contraseña.
* Validación de acceso.
* Visualización del menú principal.
* Consulta de productos.
* Consulta de usuarios.
* Gestión de información mediante servicios.
* Persistencia de datos utilizando archivos JSON.
* Manejo de productos mediante la lógica del servicio.
* Registro y manejo de ventas.
* Interfaz gráfica desarrollada con Tkinter.
* Uso de botones, contenedores y componentes gráficos.
* Uso de iconos dentro de la interfaz.
* Separación entre la interfaz gráfica y la lógica del programa.

---

## Tecnologías utilizadas

* **Python**
* **Tkinter** para la interfaz gráfica.
* **Programación Orientada a Objetos (POO)**
* **Archivos JSON** para almacenar información.
* **Visual Studio Code** para el desarrollo.
* **Git y GitHub** para el control de versiones.

---

## Estructura del proyecto

```text
semana_15/
│
├── main.py
├── README.md
├── .gitignore
│
├── assets/
│   └── icons/
│       ├── buscar.png
│       ├── cerrar sesion.png
│       ├── home.png
│       ├── menu.png
│       └── settings.png
│
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── producto.py
│   ├── usuario.py
│   ├── venta.py
│   └── _init_.py
│
├── servicios/
│   ├── archivo_servicio.py
│   ├── restaurante.py
│   ├── restaurante_servicio.py
│   └── _init_.py
│
└── ui/
    ├── login_view.py
    ├── main_view.py
    └── __init__.py
```

---

## Organización del proyecto

El proyecto se encuentra dividido en diferentes partes para mantener una mejor organización del código.

### Modelos

La carpeta `modelos` contiene las clases principales de la aplicación:

* `Producto`: representa los productos del restaurante.
* `Usuario`: representa a los usuarios registrados.
* `Venta`: representa las ventas realizadas.

### Servicios

La carpeta `servicios` contiene la lógica que permite trabajar con los datos y realizar las operaciones de la aplicación.

Entre sus archivos se encuentran:

* `archivo_servicio.py`: permite cargar y guardar información en archivos JSON.
* `restaurante.py`: contiene operaciones relacionadas con el restaurante.
* `restaurante_servicio.py`: contiene servicios utilizados por la aplicación para trabajar con productos y usuarios.

### Interfaz gráfica

La carpeta `ui` contiene las vistas de la aplicación:

* `login_view.py`: muestra la pantalla de inicio de sesión.
* `main_view.py`: muestra el menú principal y las opciones de la aplicación.

La interfaz utiliza **Tkinter** y sus diferentes componentes y contenedores.

### Datos

La carpeta `datos` almacena la información de la aplicación:

* `productos.json`
* `usuarios.json`
* `ventas.json`

Estos archivos permiten mantener la información de manera persistente.

### Assets

La carpeta `assets` contiene los recursos gráficos utilizados por la interfaz, principalmente los iconos de los botones y opciones del menú.

---

## Flujo de funcionamiento

El funcionamiento de las operaciones de la aplicación sigue una estructura organizada:

```text
Acción del usuario
       ↓
Botón de la interfaz
       ↓
command=
       ↓
Callback o función
       ↓
Servicio
       ↓
Archivo JSON
       ↓
Respuesta visual
```

De esta manera, la interfaz gráfica no contiene directamente toda la lógica del programa.

Por ejemplo, cuando el usuario realiza una acción desde un botón, la interfaz ejecuta una función que se comunica con el servicio correspondiente. El servicio realiza la operación y, cuando es necesario, guarda o consulta la información almacenada en los archivos JSON. Finalmente, el resultado se muestra nuevamente en la interfaz.

---

## Persistencia de datos

La aplicación utiliza archivos JSON para guardar la información.

Los principales archivos utilizados son:

```text
datos/productos.json
datos/usuarios.json
datos/ventas.json
```

Esto permite que los datos no se pierdan cuando se cierra el programa.

La lectura y escritura de estos archivos se encuentra separada de la interfaz gráfica mediante el archivo:

```text
servicios/archivo_servicio.py
```

---

## Interfaz gráfica

La interfaz gráfica fue desarrollada utilizando **Tkinter**.

Se utilizan diferentes componentes y contenedores para organizar las ventanas y opciones de la aplicación, entre ellos:

* Ventanas.
* Frames.
* Botones.
* Etiquetas.
* Campos de entrada.
* Áreas de visualización.
* Iconos.

Los componentes de la interfaz se encuentran principalmente dentro de la carpeta `ui`.

Los iconos utilizados se encuentran en:

```text
assets/icons/
```

---

## Programación Orientada a Objetos

El proyecto aplica diferentes conceptos de Programación Orientada a Objetos, principalmente mediante la creación de clases para representar los elementos de la aplicación.

Por ejemplo:

```text
Producto
Usuario
Venta
```

Cada clase tiene sus propios atributos y responsabilidades.

La separación en modelos y servicios permite que el código sea más organizado y facilita realizar modificaciones o agregar nuevas operaciones en el futuro.

---

## Ejecución del proyecto

Para ejecutar la aplicación se debe abrir una terminal dentro de la carpeta principal del proyecto y utilizar:

```bash
python main.py
```

También se puede ejecutar desde Visual Studio Code utilizando el archivo `main.py`.

---

## Requisitos

Para ejecutar el proyecto se necesita:

* Python instalado.
* Visual Studio Code u otro editor de código.
* Tkinter disponible en la instalación de Python.
* Los archivos JSON de la carpeta `datos`.
* Los recursos gráficos ubicados en la carpeta `assets`.

---

## Control de versiones

El proyecto utiliza **Git** para llevar el control de los cambios realizados durante el desarrollo.

El repositorio permite mantener el proyecto organizado y disponer de una copia del trabajo realizado durante la Semana 15.

---

## Conclusión

Durante la Semana 15 se continuó con el desarrollo de la aplicación Restaurante App manteniendo la estructura creada en las semanas anteriores.

Se trabajó con Programación Orientada a Objetos, interfaz gráfica mediante Tkinter, componentes y contenedores, separación de responsabilidades y persistencia mediante archivos JSON.

La organización del proyecto permite que cada parte tenga una función específica y facilita continuar agregando nuevas operaciones sin modificar completamente la estructura existente.

Con este desarrollo se refuerzan los conocimientos de Python, POO, interfaces gráficas, manejo de archivos y organización de proyectos.

---

## Autor

**Hugo Carlin Castillo Calva**

**Proyecto académico – Semana 15**
