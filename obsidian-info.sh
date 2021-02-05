#!/bin/bash
cd /Users/crow/Dropbox/Obsidian-vaults/RavenNest


WORD=$(wc *.md | tail -1 | awk '$1 ~ /[0-9]/ {print $2}')
printf "Words written: \t\t%'d\n" $WORD

NOTES=$(wc *.md | wc | awk '$1 ~ /[0-9]/ {print $1}')
NOTES=$((NOTES-1))
printf "Total notes: \t\t%'d\n" $NOTES

AVGWORDS=$((WORD/NOTES))
printf "Average words per note:\t%'d\n" $AVGWORDS

WEEKNOTES=$(wc *Weeknotes*.md | wc | awk '$1 ~ /[0-9]/ {print $1}')
WEEKNOTES=$((WEEKNOTES-1))
printf "Weeknotes: \t\t%'d\n" $WEEKNOTES

LINKS=$(grep -c http *.md | awk -F ":" '{sum += $NF} END {print sum}')
printf "Number of links: \t%'d\n" $LINKS
