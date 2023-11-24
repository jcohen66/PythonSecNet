import subprocess

program = input("Enter a process in your operating system: ")
process = subprocess.run(['which', program], capture_output=True, text=True)
if process.returncode != 0:
    print(f"[-] Sorry, the {program} is not installed.")
    exit(1)
else:
    print(f"[+] The {program} is installed.")
    print(f"[+] The path of {program} is: {process.stdout}")
    exit(0)