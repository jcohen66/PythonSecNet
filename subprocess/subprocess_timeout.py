import subprocess
import sys
"""
If we run the process using subprocess.run(), our parent process hangs for as long as it takes
for the child process to return the response. Once the thread is launched, our main process blocks
and only continues when the thread terminates. The method subprocess.run() includes the
timeout argument to allow you to stop an external program if it takes too long to execute.
"""
result = subprocess.run([sys.executable, '-c', "import time; time.sleep(10)"], timeout=5)