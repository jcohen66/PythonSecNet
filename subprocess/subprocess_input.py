import subprocess
import sys

"""
The input argument can be useful if you want to chain multiple invocations by
passing the output of one process as the input of another.
"""

result = subprocess.run(
 [sys.executable, "-c", "import sys; print(sys.stdin.read())"],input=b"python"
)
print(result.returncode)
