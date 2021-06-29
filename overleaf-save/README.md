# Overleaf Save

This is a script that uses Selenium to automatically log in to Overleaf,
find a project by its UID, and download it as a zip. The shell script then
unzips the file to a specified location, and git commits the changes to a
repository.

I wrote this for a bit of yak shaving while I was working on a group project
that required working in \LaTeX, and didn't want to pay for the premium
Overleaf membership in order to have git tracking. The  script could be run
manually whenever I had made some changes, or on a crontab basis.

I wasn't able to get it running effectively headless, so it opens up the
browser window in order to function. Good fun playing around with Selenium
and learning browser automation for a purpose
