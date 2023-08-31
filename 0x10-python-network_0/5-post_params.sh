#!/bin/bash
# script that post to server request
curl -sLX POST -d "email: test@gmail.com" -d "subject: I will always be here for PLD" $1
