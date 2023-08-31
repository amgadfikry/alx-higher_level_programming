#!/bin/bash
# script for get lenght of conent in curl request
curl -s -i $1 | grep -i 'content-length' | cut -d ' ' -f 2
