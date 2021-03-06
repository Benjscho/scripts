# Overleaf Save

This is a script that uses Selenium to automatically log in to Overleaf,
find a project by its UID, and download it as a zip. The shell script then
unzips the file to a specified location, and git commits the changes to a
repository.

I wrote this for a bit of yak shaving while I was working on a group project
that required working in LaTeX, and didn't want to pay for the premium
Overleaf membership in order to have git tracking. The  script could be run
manually whenever I had made some changes, or on a crontab basis.

I wasn't able to get it running effectively headless, so it opens up the
browser window in order to function. Good fun playing around with Selenium
and learning browser automation for a purpose

## Usage

To use create a file named `creds.py` that contains a dictionary object
with the variables 'OL\_USERNAME' and 'OL\_PASSWORD' respectively. It should
look like:

```python
login = {
	'OL_USERNAME':'<username here>',
	'OL_PASSWORD':'<password here>'
}
```

Install the requirements with `pip install -r requirements.txt`, and download a
version of the [chromium web driver from
here](https://sites.google.com/chromium.org/driver/downloads?authuser=0).  The
web driver should be in the same folder, although its location can be edited in
the `main.py` file.

## Blocked

Update since I last used it, just tried to test again and I'm getting a
captcha response from Overleaf after the login, not sure whether its possible
to get around that one but it was fun to do before.
