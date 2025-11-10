# 🧠 Portafolio de Análisis de Datos  
**Autor:** Daniel Aguiñaga  

---

## 📌 Descripción
Este repositorio contiene los proyectos desarrollados durante el programa **TripleTen - Análisis de Datos**.  
Cada carpeta incluye un **Jupyter Notebook (`.ipynb`)** con el desarrollo completo de cada sprint y los **datasets (`.csv`)** correspondientes.  
Además, se proporciona un entorno virtual configurado para garantizar la reproducibilidad de los resultados.


## ⚙️ 1. Preparación del entorno

### 📁 Estructura esperada del repositorio
```
Portafolio_Analisis_de_Datos/
├─ setup_env.py
├─ requirements.txt o requirements_generated.txt
├─ requirements.lock.txt  ← (se genera automáticamente)
├─ data/                  ← (datasets compartidos)
├─ Proyecto_Sprint_1_Daniel_Aguinaga.ipynb
├─ Proyecto_Sprint_2_Daniel_Aguinaga.ipynb
├─ Proyecto_Sprint_3_Daniel_Aguinaga.ipynb
├─ Proyecto_Sprint_4_Daniel_Aguinaga.ipynb
├─ Proyecto_Sprint_5_Daniel_Aguinaga.ipynb
└─ Proyecto_Sprint_6_Daniel_Aguinaga.ipynb
```

---

## 🧩 2. Configuración automática del entorno

> 🟢 Este paso debe hacerse **una sola vez**.  
> Configura el entorno virtual `.venv`, instala todas las librerías necesarias y registra el kernel de Jupyter.

### ▶️ Ejecución del script de instalación

Abre una terminal y ejecuta:

```bash
cd "/Users/daniela./Documents/Triple Ten/Portafolio_Analisis_de_Datos"
python setup_env.py
```

El script realiza automáticamente:
1. Creación de un entorno virtual `.venv`
2. Instalación de dependencias desde `requirements.txt` o `requirements_generated.txt`
3. Registro del kernel de Jupyter llamado **`portafolio`**
4. Creación del archivo `requirements.lock.txt` con las versiones exactas

---

## 🧠 3. Activar el entorno virtual

Cada vez que quieras trabajar en tus proyectos:

### En macOS / Linux
```bash
cd "/Users/daniela./Documents/Triple Ten/Portafolio_Analisis_de_Datos"
source .venv/bin/activate
```

### En Windows PowerShell
```bash
cd "C:\Users\daniela.\Documents\Triple Ten\Portafolio_Analisis_de_Datos"
.venv\Scripts\activate
```

---

## 💻 4. Ejecutar los notebooks

Una vez activado el entorno:

```bash
jupyter lab
```

1. Abre cualquiera de los notebooks del repositorio:
   - `Proyecto_Sprint_1_Daniel_Aguinaga.ipynb`
   - `Proyecto_Sprint_2_Daniel_Aguinaga.ipynb`
   - `...`  
2. Selecciona el kernel **`portafolio`** si Jupyter lo solicita.
3. Ejecuta las celdas secuencialmente (Shift + Enter).

---

## 📦 5. Añadir nuevas librerías (opcional)

Si instalas nuevas dependencias, actualiza el archivo de bloqueo con:

```bash
pip install nombre_libreria
pip freeze > requirements.lock.txt
```

Así, todos los usuarios tendrán el mismo entorno cuando ejecuten `setup_env.py`.

---

## 🧪 6. Solución de problemas comunes

| Problema | Solución |
|-----------|-----------|
| `ModuleNotFoundError` | Activa el entorno `.venv` antes de ejecutar Jupyter. |
| `Kernel not found` | Ejecuta `python -m ipykernel install --user --name portafolio` |
| `Permission denied` (macOS) | Usa `python3 setup_env.py` en lugar de `python setup_env.py` |
| Error de CSV o ruta | Usa rutas relativas (`./data/archivo.csv`) en los notebooks. |

---

## 📈 7. Reproducibilidad garantizada

Este repositorio incluye:
- `requirements_generated.txt` → dependencias generales.  
- `requirements.lock.txt` → versiones exactas del entorno instalado.  
- `setup_env.py` → script universal de configuración.

Cualquier usuario podrá replicar el entorno con un solo comando:
```bash
python setup_env.py
```

---

## 🧾 8. Créditos y Licencia
**Autor:** Daniel Aguiñaga  
**Última actualización:** 2025-11-10
