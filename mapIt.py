#! python3
# mapTi.py - Launche a map in the browser using and address from the
# command line or clipboard.

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
  # Get address from commad line.
  address = ' '.join(sys.argv[1:])
else:
  # Get address from clipboard.
  address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
