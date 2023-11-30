#!/bin/bash
# Bash script that takes a URL and displays the body size.
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
