import requests
import os
import subprocess

#get lastest commit hash
#if our git hash is not equal, pull latest
#do this every 5min
def main():
    local_hash = subprocess.check_output(["git", "rev-parse", "HEAD"])
    remote_hash = subprocess.check_output(["git", "log", "-n", "1"])
    print(local_hash)
    print(remote_hash) 


