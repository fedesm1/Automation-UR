# Federico Suarez Moreno, Cohort 13

# Urban Routes Testing Project

# Descripción

Este proyecto contiene pruebas automatizadas para la aplicación web de Urban Routes, en donde se realizan 
algunos pasos del servicio de pedido de taxis, se prueban características de la funcionalidad de la aplicación, 
como la configuración de rutas, selección de tarifas, ingreso de información de contacto, métodos de pago y opciones adicionales para el viaje.

# Tecnologías

- Python: Lenguaje de programación principal.
- Selenium WebDriver: Framework de automatización.
- PyTest: Librería para pruebas.

# Técnicas

- Page Object Model (POM): Patrón de diseño utilizado para crear una representación orientada a objetos de las páginas web.
- Esperas Explícitas: Técnica utilizada para manejar elementos asincrónicos en la página web.


## Instrucciones para Ejecutar las Pruebas

1. Tener Python instalado.
2. Instalar las librerías: Selenium & Pytest
3. Instalar ChromeDriver y configurar el PATH del sistema.

# Estructura

- Archivos: 
1. data.py, guarda datos importantes para la interacción con la página web, como la URL y datos de entrada para formularios.
2. main.py, contiene las clases, importaciones y funciones necesarias para ejecutar las pruebas.
3. README.md, contiene los detalles del proyecto.