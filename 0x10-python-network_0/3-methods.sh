#!/bin/bash
# script show methods can use on this url
curl -si $1 | grep -i "allow" | cut -d " " -f 2-
