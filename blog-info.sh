#!/bin/bash

# wc `find /Users/crow/Dropbox/benjscho/_posts/ -type f`

WORD=$(wc `find /Users/crow/Dropbox/benjscho/_posts/ -type f` | tail -1 | awk '$1 ~ /[0-9]/ {print $2}')
echo "${WORD} words written"
NOTES=$(wc `find /Users/crow/Dropbox/benjscho/_posts/ -type f` | wc | awk '$1 ~ /[0-9]/ {print $1}')

# Account for added line
NOTES=$((NOTES-1))
echo "${NOTES} total posts"
