#!/usr/bin/python3
"""
    Module that akes in a URL and an email address, sends a POST request
    to the passed URL with the email as a parameter,
    and finally displays the body of the response.
"""
from requests import post
from sys import argv


if __name__ == "__main__":
    content = post(argv[1], data={'email': argv[2]})
    print(content.text)
