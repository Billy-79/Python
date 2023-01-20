#!/usr/bin/env python3


import subprocess

svc = "sshd"

service_check = subprocess.call(["ps", "-C", svc])

if service_check == 0:
    print("The service is running.")
else:
    print("The service is NOT running.")
    print("Starting it...")
    subprocess.call(["systemctl", "start", "sshd"])
    subprocess.call(["ps", "-C", svc])
