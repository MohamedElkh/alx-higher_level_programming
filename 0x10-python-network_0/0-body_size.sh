#!/bin/bash
#get the byte size of http response

curl -s "$1" | wc -c
