#!/bin/bash
cd /Users/crow/Dropbox/Obsidian-vaults/RavenNest

WORD=$(wc *.md | tail -1 | awk '$1 ~ /[0-9]/ {print $2}')
echo -e "Words written: \t\t${WORD}"

NOTES=$(wc *.md | wc | awk '$1 ~ /[0-9]/ {print $1}')
NOTES=$((NOTES-1))
echo -e "Total notes: \t\t${NOTES}"

AVGWORDS=$((WORD/NOTES))
echo -e "Average words per note:\t${AVGWORDS}"

WEEKNOTES=$(wc *Weeknotes*.md | wc | awk '$1 ~ /[0-9]/ {print $1}')
WEEKNOTES=$((WEEKNOTES-1))
echo -e "Weeknotes: \t\t${WEEKNOTES} "
