#!/bin/bash
# A bash script that ends a request to a URL passed and displays status code.
curl -so /dev/null -w "%{http_code}" "$1"
