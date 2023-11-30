#!/bin/bash
# A bash script that ends a JSON POST request to a URL passed and displays body
curl -sX POST -H "Content-Type: application/json" -d @$2 "$1"
