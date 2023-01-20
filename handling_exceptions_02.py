#!/usr/bin/env python3


import subprocess

svc = "sshd"

check_cmd = ["ps",
             "-C",
             svc]

service_check = subprocess.call(check_cmd)

if service_check == 0:
    print("The service is running.")
else:
    print("The service is NOT running.")
    print("Starting it...")
    try:
        subprocess.call(["systectl", "start", "sshd"])
    except:
        print("There was an error starting the process.")
    subprocess.call(check_cmd)
