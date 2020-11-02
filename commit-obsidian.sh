#!/bin/bash
# Git: add and commit changes
cd /Users/crow/Dropbox/Obsidian-vaults/RavenNest && /usr/local/bin/git add --all && /usr/local/bin/git commit -m "daily crontab backup `date`"

# Zip folder and backup
cd /Users/crow/Dropbox/Obsidian-vaults/ && zip -r RavenNest-backup.zip /Users/crow/Dropbox/Obsidian-vaults/RavenNest
mv /Users/crow/Dropbox/Obsidian-vaults/RavenNest-backup.zip "/Users/crow/Library/Mobile Documents/com~apple~CloudDocs/Obsidian Backups"
