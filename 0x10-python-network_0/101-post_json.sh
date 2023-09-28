#!/bin/bash
#send a json post request to the url and display the body of response
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
