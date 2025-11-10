#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path

REPO_ROOT = Path.cwd()
VENV_DIR = REPO_ROOT / ".venv"

def run(cmd, check=True):
    print(f"\n$ {' '.join(cmd)}")
    return subprocess.run(cmd, check=check)

def venv_python_path():
    if os.name == "nt":
        return VENV_DIR / "Scripts" / "python.exe"
    else:
        return VENV_DIR / "bin" / "python"

def venv_pip_path():
    if os.name == "nt":
        return VENV_DIR / "Scripts" / "pip.exe"
    else:
        return VENV_DIR / "bin" / "pip"

def ensure_venv():
    if VENV_DIR.exists():
        print(f"✅ Entorno virtual encontrado: {VENV_DIR}")
    else:
        print("🆕 Creando entorno virtual .venv ...")
        run([sys.executable, "-m", "venv", str(VENV_DIR)])
    py = venv_python_path()
    if not py.exists():
        raise SystemExit("❌ No se encontró el ejecutable de Python dentro del .venv.")
    return py

def pick_requirements_file():
    candidates = [
        REPO_ROOT / "requirements.txt",
        REPO_ROOT / "requirements_generated.txt",
    ]
    for c in candidates:
        if c.exists():
            print(f"📄 Usando archivo de requisitos: {c}")
            return c
    minimal = REPO_ROOT / "requirements.txt"
    print("⚠️ No se encontró ningún archivo de requisitos. Creando uno mínimo...")
    minimal.write_text(
        "jupyterlab\nipykernel\npandas\nnumpy\nmatplotlib\nseaborn\nscikit-learn\n",
        encoding="utf-8",
    )
    return minimal

def install_requirements(pip_path, req_file):
    print("⬇️ Instalando dependencias ...")
    run([str(pip_path), "install", "--upgrade", "pip", "setuptools", "wheel"])
    run([str(pip_path), "install", "-r", str(req_file)])

def register_kernel(py_path, kernel_name="portafolio"):
    print(f"🧠 Registrando kernel de Jupyter: {kernel_name}")
    run([str(py_path), "-m", "ipykernel", "install", "--user", "--name", kernel_name])

def lock_requirements(pip_path):
    lock_file = REPO_ROOT / "requirements.lock.txt"
    print(f"🔒 Exportando versiones instaladas a {lock_file}")
    proc = subprocess.run([str(pip_path), "freeze"], check=True, capture_output=True, text=True)
    lock_file.write_text(proc.stdout, encoding="utf-8")

def main():
    print("🔧 Configuración automática del entorno para el portafolio\n")
    py_path = ensure_venv()
    pip_path = venv_pip_path()

    if not pip_path.exists():
        print("⚠️ pip no encontrado dentro del entorno; intentando asegurarlo...")
        run([str(py_path), "-m", "ensurepip", "--upgrade"], check=False)

    req_file = pick_requirements_file()
    install_requirements(pip_path, req_file)
    register_kernel(py_path, kernel_name="portafolio")
    lock_requirements(pip_path)

    print("\n✅ Todo listo.")
    print("👉 Para usar el entorno:")
    if os.name == "nt":
        print(r"   .venv\Scripts\activate")
    else:
        print("   source .venv/bin/activate")
    print("👉 Luego ejecuta: jupyter lab")
    print("👉 En cada notebook, selecciona el kernel: portafolio")

if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Falló un comando: {e}")
        sys.exit(e.returncode)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
