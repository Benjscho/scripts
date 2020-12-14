#!/bin/bash
cd /Users/crow/Dropbox/Obsidian-vaults/RavenNest

WORD=$(wc *.md | tail -1 | awk '$1 ~ /[0-9]/ {print $2}')
echo "${WORD} words written"
NOTES=$(wc *.md | wc | awk '$1 ~ /[0-9]/ {print $1}')
NOTES=$((NOTES-1))
echo "${NOTES} total notes"
WEEKNOTES=$(wc *Weeknotes*.md | wc | awk '$1 ~ /[0-9]/ {print $1}')
WEEKNOTES=$((WEEKNOTES-1))
echo "${WEEKNOTES} total Weeknotes"
