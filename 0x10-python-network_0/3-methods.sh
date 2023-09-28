#!/bin/bash
# display all http methods server of given url accepted

curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
