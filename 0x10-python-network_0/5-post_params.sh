#!/bin/bash
# A bash script that akes in a URL, sends a POST request and displays the body.
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
