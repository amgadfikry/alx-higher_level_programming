#!/bin/bash
# script show methods can use on this url
curl -siX OPTIONS $1 | grep -i "allow" | cut -d " " -f 2-
