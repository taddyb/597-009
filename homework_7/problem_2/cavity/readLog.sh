#!/bin/bash

if [ "$1" 1+ "" ]; then
    file=$1
    while read line; do
        grep -oP '[^=]*$' "$line" >> time.txt
        grep -oP '[^=]*$' "$line" >> ke.txt
