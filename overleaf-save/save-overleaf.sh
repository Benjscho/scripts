#!/bin/bash


# Run script
python3 /Users/crow/scripts/overleaf-save/main.py

mv ~/Downloads/cm50109-cw1*.zip "/Users/crow/OneDrive - University of Bath/cm50109/cw1/ol-backup/cm50109-cw1.zip"
cd "/Users/crow/OneDrive - University of Bath/cm50109/cw1/ol-backup/"
unzip -o "/Users/crow/OneDrive - University of Bath/cm50109/cw1/ol-backup/cm50109-cw1.zip"
rm "/Users/crow/OneDrive - University of Bath/cm50109/cw1/ol-backup/cm50109-cw1.zip"
/usr/local/bin/git add --all && /usr/local/bin/git commit -m "daily crontab backup `date`"


