#!/bin/bash

LINES=$(wc $1 | awk '{print $1}')
if [ $LINES -gt 9 ]
then
    head -n 10 $1 | tail -n 1
fi
