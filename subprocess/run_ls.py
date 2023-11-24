import subprocess

process = subprocess.run(('ls', '-la'), stdout=subprocess.PIPE)
print(process.stdout.decode('utf-8'))

try:
    process = subprocess.run(('find', '/folder_not_exists'), stdout=subprocess.PIPE, check=True)
    print(process.stdout.decode('utf-8'))
except subprocess.CalledProcessError as error:
    print(f"[-] Error: {error}")

