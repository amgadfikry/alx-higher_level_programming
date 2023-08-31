#!/bin/bash
# script add json file to post request
curl -s -X POST -H "Content-Type: application/json" -d @$2 $1
