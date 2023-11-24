import sys
import os

# Check if file exists and whether it is accessible.
print(len(sys.argv))
if (len(sys.argv) >= 2):
    filename = sys.argv[1]
    if os.path.isfile(filename):
        print(f"[+] {filename} File exists")
    else:
        print(f"[-] {filename} File does not exist")
        exit(0)
    if not os.access(filename, os.R_OK):
        print(f"[-] {filename} File is not accessible")
        exit(0)