#!/usr/bin/python3
"""
    Module that fetches header id body response.
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    response = get(argv[1])
    print(response.headers.get('X-Request-Id'))
