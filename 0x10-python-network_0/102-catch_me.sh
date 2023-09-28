#!/bin/bash
#make a request to 0000:5000 that gets the message
curl -sL -X Put -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
