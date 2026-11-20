<div align="center">

# 👥 Registro Básico de Empleados

**Sistema Modular de Gestión y Administración de Personal en Python**

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

</div>

---

## 📖 Descripción

**Registro Básico de Empleados** es una aplicación de terminal desarrollada en **Python 3** diseñada para gestionar de forma eficiente el ciclo de vida de los registros de personal en una organización.

El proyecto aplica una arquitectura modular que separa la interfaz de usuario en consola, el almacenamiento en memoria y los servicios de lógica de negocio, incorporando validaciones defensivas contra errores de entrada de usuario (`try/except`).

---

## 🚀 Características Principales

- **Gestión CRUD Completa:**
  - **Agregar empleado:** Registro con ID numérico único, validación de valores positivos y prevención de duplicados.
  - **Listar empleados:** Reporte estructurado con la información de todos los colaboradores registrados.
  - **Buscar empleado:** Búsqueda puntual mediante número de identificación.
  - **Actualizar empleado:** Modificación dinámica de los datos del colaborador.
  - **Eliminar empleado:** Baja controlada de registros existentes.
- **Arquitectura Modular:** Separación limpia de responsabilidades:
  - `app.py`: Controlador principal del bucle de menú de opciones.
  - `employees.py`: Estructura y almacenamiento del estado en memoria.
  - `services.py`: Lógica de validación, reglas de negocio y operaciones sobre los datos.
- **Manejo Preventivo de Excepciones:** Control de entradas inválidas mediante bloques `try / except ValueError`.

---

## 📂 Estructura del Proyecto

```text
RegistroBasicoDeEmpleados/
├── LICENSE                 # Licencia MIT
├── README.md               # Documentación del proyecto
└── src/
    ├── app.py              # Menú interactivo y ejecución principal
    ├── employees.py        # Almacén de datos en memoria
    └── services.py         # Servicios CRUD y validaciones
```

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**

---

## ⚙️ Puesta en Marcha

### 1. Clonar el repositorio
```bash
git clone https://github.com/Danilo-Doria/RegistroBasicoDeEmpleados.git
cd RegistroBasicoDeEmpleados
```

### 2. Ejecutar la aplicación
```bash
python3 src/app.py
```

### 3. Opciones del Menú
Una vez iniciada la aplicación, podrás seleccionar:
1. Agregar empleado
2. Mostrar empleados
3. Buscar empleado
4. Actualizar empleado
5. Eliminar empleado
6. Salir

---

## 👨💻 Author

- GitHub: **[Danilo-Doria](https://github.com/Danilo-Doria)**
- LinkedIn: **[Danilo Doria Diaz](https://www.linkedin.com/in/danilo-doria-diaz)**
- Mail: **danilodoria519@gmail.com**

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
