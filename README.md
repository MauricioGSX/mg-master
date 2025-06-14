# MG Master V1.5

### SISTEMA DE GESTIÓN PARA RESERVAS (https://mg-master.onrender.com)
El sistema MG Master ha sido desarrollado con fines exclusivamente educativos y de aprendizaje. Todos los mensajes de depuración se han mantenido por esta misma razón. Se prohíbe su distribución o venta. Si tiene alguna sugerencia o idea que pueda contribuir al proyecto, no dude en ponerse en contacto con nosotros.

### USUARIOS DE PRUEBA
- **Rol Usuario**:
  - Username: `usuario`
  - Contraseña: `contraseña123`
- **Rol Recepcionista**:
  - Username: `recepcionista`
  - Contraseña: `contraseña123`

## **Vista de imágenes**

<div style="display: flex; gap: 10px;">
  <a href="https://i.ibb.co/5Mcd03V/5.png" target="_blank"><img src="https://i.ibb.co/5Mcd03V/5.png" width="100" height="100"></a>
  <a href="https://i.ibb.co/PjtjMcN/4.png" target="_blank"><img src="https://i.ibb.co/PjtjMcN/4.png" width="100" height="100"></a>
  <a href="https://i.ibb.co/PNMXrrx/3.png" target="_blank"><img src="https://i.ibb.co/PNMXrrx/3.png" width="100" height="100"></a>
  <a href="https://i.ibb.co/gjnZT1c/2.png" target="_blank"><img src="https://i.ibb.co/gjnZT1c/2.png" width="100" height="100"></a>
  <a href="https://i.ibb.co/Zz8YT2T/1.png" target="_blank"><img src="https://i.ibb.co/Zz8YT2T/1.png" width="100" height="100"></a>
</div>

## Índice

- [Tecnologías utilizadas](#tecnologías-utilizadas)
- [Contacto](#contacto)
- [Changelog](#changelog)
- [Características](#características)
- [Instalación](#instalación)
- [Vista de imágenes](#vista-de-imágenes)
- [Licencia](#licencia)


## **Tecnologías utilizadas**
<div align="center" style="display: flex; flex-wrap: wrap; gap: 10px; justify-content: center;">
  <img alt="Python Version" src="https://img.shields.io/pypi/pyversions/bing-rewards?style=flat-square&label=Python&logo=python&logoColor=yellow">
  <a href="https://pypi.org/project/bing-rewards/"><img alt="Django Version" src="https://img.shields.io/badge/Django-4.2.16-0A73B7?style=flat-square&logo=django&logoColor=white" ></a>
  <img alt="License" src="https://img.shields.io/pypi/l/bing-rewards?style=flat-square&label=License&color=blueviolet">
  <img alt="htmx" src="https://img.shields.io/badge/htmx-1.9.12-brightgreen?style=flat-square" >
  <img alt="Flowbite" src="https://img.shields.io/badge/Flowbite-2.3.0-blue?style=flat-square" >
<img alt="Bootstrap Versions" src="https://img.shields.io/badge/Bootstrap-4.5.2%20|%205.0-lightblue?style=flat-square">
  <img alt="jQuery 3.7.1" src="https://img.shields.io/badge/jQuery-3.7.1-lightgrey?style=flat-square" >
  <img alt="Jinja2" src="https://img.shields.io/badge/Jinja2-3.0.0-darkorange?style=flat-square" >
  <img alt="Font Awesome 6.0.0" src="https://img.shields.io/badge/Font%20Awesome-6.0.0-purple?style=flat-square">
  <img alt="Select2" src="https://img.shields.io/badge/Select2-4.0.6-lightgreen?style=flat-square">
</div>

## **Contacto**

Si tienes alguna pregunta, sugerencia o deseas contribuir al proyecto, no dudes en ponerte en contacto a través de los siguientes medios:

- **Correo electrónico**: [mau.gonzalezs9315@gmail.com](mailto:mau.gonzalezs9315@gmail.com)
- **GitHub**: [https://github.com/MauricioGSX](https://github.com/MauricioGSX)


---

## 👥 Usuarios de Prueba

Utiliza los siguientes usuarios para probar el sistema:

| Rol            | Usuario    | Clave         |
|----------------|------------|---------------|
| Demo           | `demo`     | `demo123456`  |
| Recepcionista  | `recepcion`| `Recep123`    |

---

## **Changelog**

### v1.5 (2025-06-12)
- **Changed**: 
  - Implementación de WebSocket con **ASGI** usando el servidor **Daphne**.  
  - Corrección de documentación y resolución de errores.  
  - Mejora en la seguridad de todo el sistema.  
  - Rediseño de la **NavBar** y de varias secciones para optimizar la experiencia visual.


### v1.0 (2024-11-13)
- **Lanzamiento inicial**: 
  - Implementación de autenticación de usuarios, gestión de vehículos, citas, y servicios.
  - Funcionalidad básica de gestión de mecánicos, sucursales y canje de puntos.
  - Paneles de usuario y recepcionista.

### v0.9 (2024-10-15)
- **Primera versión beta**:
  - Funciones iniciales de autenticación de usuarios.
  - Registro de vehículos y citas.
  - Interfaz básica de administración.

---
## **Características**

- **Autenticación de usuarios**: 
  - Inicia sesión, regístrate y cierra sesión mediante vistas personalizadas.

- **Gestión de vehículos**: 
  - Permite registrar, actualizar y eliminar vehículos, así como obtener modelos por marca.

- **Gestión de citas**: 
  - Crear, ver, y actualizar el estado de las citas, incluyendo la posibilidad de actualizar listas de verificación.

- **Gestión de mecánicos y sucursales**: 
  - Administrar mecánicos, sus detalles, y sucursales de trabajo.

- **Canje de puntos**: 
  - Los usuarios pueden canjear puntos por premios u otros beneficios.

- **Paneles de usuario y recepcionista**: 
  - Diferentes vistas y menús para usuarios y recepcionistas, adaptados a sus roles.

- **Configuración de cuenta**: 
  - Los usuarios pueden cambiar configuraciones de su cuenta, actualizar su perfil y modificar su contraseña.

- **Servicios y trabajos**: 
  - Gestión de los servicios ofrecidos y trabajos realizados en los vehículos.

---

## **Instalación**

### Paso 1: Clonar el repositorio

1. **Clonar el repositorio**:
   - Se usa el comando `git clone` para clonar el repositorio desde un repositorio remoto a tu máquina local:
     ```bash
     git clone https://github.com/MauricioGSX/mg-master
     ```

### Paso 2: Construir y levantar el contenedor

1. **Construir y ejecutar el contenedor Docker**:
   - Una vez que hayas clonado el repositorio, navega al directorio donde se encuentra el archivo `docker-compose.yml` y ejecuta el siguiente comando para construir y ejecutar el contenedor Docker:
     ```bash
     cd /ruta/a/tu/proyecto
     docker-compose --build
     docker-compose up
     ```

### Paso 3: Mover la base de datos (si es necesario)

Si la base de datos `db.sqlite3` ya está dentro del contenedor y necesitas moverla a la raíz del contenedor, sigue estos pasos:

1. **Acceder al contenedor**:
   - Abre **Docker Desktop** y selecciona el contenedor en ejecución.
   - Haz clic en **"CLI"** o, alternativamente, accede al contenedor usando el siguiente comando:
     ```bash
     docker exec -it <nombre_del_contenedor> /bin/bash
     ```

2. **Mover el archivo de la base de datos**:
   - Dentro del contenedor, ejecuta el siguiente comando para mover el archivo `db.sqlite3` desde la carpeta `/app/` a la raíz del contenedor:
     ```bash
     mv /app/db.sqlite3 /db.sqlite3
     ```

### Notas adicionales

- Si deseas detener el contenedor, puedes usar:
  ```bash
  docker-compose down

---

## **Licencia**

Este proyecto está bajo la licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

---
