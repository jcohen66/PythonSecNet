import subprocess
import sys

result = subprocess.run([sys.executable, '-c', "raise ValueError('Oops!')"], check=True)