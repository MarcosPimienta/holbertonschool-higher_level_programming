#!/bin/bash
# Displays the size of the body of the response
curl -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
