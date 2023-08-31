#!/bin/bash
# script that display state code of request
curl -s -o /dev/null -w "%{http_code}" $1
