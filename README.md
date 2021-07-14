# Scripts

This is a repo for any scripts that will hopefully make my life easier.

## Commit Obsidian
This script is one line that runs at 06:30 am every day via crontab to stage
and commit any changes to my Obsidian notebook. This means I'll have version
tracked daily versions.

## `wc-code`
This is a one liner from somewhere that takes in a regex and finds all files
that match it in the current directory and subdirectories before passing them
to wordcount.

Example usage:
```bash
wc-code "*.py"
```
This would get the word count for all python files in any subdirectories.

Considering adding the ability to select languages to check? Otherwise might
be better termed `wc-regex`.

## `obsidian-info`

This is a neat little script that looks at my Obsidian vault and prints out
some stats for me, including total notes, total words written, average words
per note, etc.

## `remove-spaces`

Does what it says on the tin. Removes spaces from the filenames of all files
in a directory and replaces them with underscores "\_".

## `glstats`

Gives me commit stats on my git repos. Summarises how many additions and
deletions have been made. Could be edited so it can take any author instead
of just doing me by default.
