#!/bin/bash
# script show methods can use on this url
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
