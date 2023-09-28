#!/bin/bash
#send a request to the url and display only the status code of res
curl -s -o /dev/null -w "%{http_code}" "$1"
