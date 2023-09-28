#!/bin/bash
#send a post request to the passed url

curl -s -X Post -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
