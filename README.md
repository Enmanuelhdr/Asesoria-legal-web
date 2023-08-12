# Página Web de Asesorías y Pruebas de Automatización

Este repositorio contiene una página web diseñada para ofrecer asesorías, utilizando el framework CSS Bootstrap para mejorar la apariencia y la experiencia del usuario. Además, se incluye un conjunto de pruebas de automatización utilizando Selenium y Python, enfocadas en interactuar con la página web y extraer datos de archivos JSON para realizar pruebas exhaustivas del formulario.

## Contenido

- [Características](#características)
- [Requisitos](#requisitos)
- [Instrucciones de Uso](#instrucciones-de-uso)
- [Configuración de Pruebas de Automatización](#configuración-de-pruebas-de-automatización)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Características

- Diseño de la página web de asesorías utilizando el framework CSS Bootstrap para una apariencia moderna y responsiva.
- Formulario interactivo para que los usuarios ingresen información.
- Automatización de pruebas utilizando Selenium en el navegador Chrome.
- Extracción de datos de archivos JSON para realizar pruebas exhaustivas del formulario.

## Requisitos

- Navegador web (se recomienda Google Chrome)
- Python 3.x instalado
- Bibliotecas Python: selenium

## Instrucciones de Uso

1. Clona este repositorio en tu máquina local.
2. Abre el archivo `index.html` en tu navegador para explorar la página web de asesorías.
3. Configura el entorno virtual de Python y asegúrate de tener instalada la biblioteca `selenium`.
4. Ejecuta los scripts de prueba en la carpeta `tests` utilizando comandos como `python test_form_submission.py`.

### Importaciones de libreria a realizar
[![Importaciones.png](https://i.postimg.cc/7LWZjyGh/Importaciones.png)](https://postimg.cc/SXc4z3Gb)

## Configuración de Pruebas de Automatización

1. Asegúrate de tener el controlador de Chrome WebDriver instalado y en la ruta adecuada.
2. Edita los archivos de prueba en la carpeta `tests` según sea necesario para adaptar las pruebas a tus requerimientos.
3. Los archivos JSON en la carpeta `data` contienen registros de prueba para simular entradas de usuarios en el formulario.

## Video demostrativo de las pruebas realizadas en la pagina de citas y sugerencias
https://youtu.be/XPyy1Fm8DOg

## Capturas de pruebas realizadas
### citas
[![Prueba-citas-asesoria.png](https://i.postimg.cc/667YkVSp/Prueba-citas-asesoria.png)](https://postimg.cc/vDsr9nbJ)
### sugerencias
[![Prueba-sugerencias.png](https://i.postimg.cc/85fzSnMH/Prueba-sugerencias.png)](https://postimg.cc/CBYgC7vB)

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar la página web, las pruebas o agregar nuevas características, ¡siéntete libre de hacerlo! Solo asegúrate de seguir las mejores prácticas de desarrollo y hacer una solicitud de extracción.

## Licencia

Este proyecto está bajo la Licencia [MIT](LICENSE).
