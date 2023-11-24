import subprocess
from pathlib import Path

"""
The main advantage of using these modules is that they allow us to abstract ourselves from the
operating system and we can perform different operations regardless of the operating system
we are using.
"""

VENV_NAME= '.venv'
REQUIREMENTS_FILE = 'requirements.txt'

process = subprocess.run(['which', 'python3'], capture_output=True, text=True)
if process.returncode != 0:
    raise OSError(f"[-] Sorry, the python3 is not installed.")
python_process = process.stdout.strip()
print(f"[+] Python found in: {python_process}")

process = subprocess.run('echo "$SHELL"', shell=True, capture_output=True, text=True)
shell_bin = process.stdout.split('/')[-1]
create_venv = subprocess.run([python_process, '-m', 'venv', VENV_NAME],check=True)
if create_venv.returncode == 0:
    print(f"[+] Virtual environment {VENV_NAME} created.")
else:
    raise OSError(f"[-] Sorry, the virtual environment {VENV_NAME} could not be created.")

pip_process = Path(VENV_NAME) / 'bin' / 'pip'
if Path(REQUIREMENTS_FILE).exists():
    print(f"Requirements file {REQUIREMENTS_FILE} found.")
    print("Installing requirements...")
    install_requirements = subprocess.run([pip_process, 'install', '-r', REQUIREMENTS_FILE],check=True)
print('Process completed! Now activate your environment with "source .venv/bin/activate')