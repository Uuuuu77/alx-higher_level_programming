#!/usr/bin/python3
"""
    Module that fetches an email as response.
"""
from urllib.request import urlopen
from sys import argv


if __name__ == "__main__":
    data = f"email={argv[2]}".encode('utf-8')
    with urlopen(argv[1], data=data) as response:
        content = response.read().decode('utf-8')
        print(content)
