#! python3
# lucky.py - Opnes several Google search results.

import requests, bs4, webbrowser,sys

print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open a browser tag for each result.
linkElms = soup.select('.r a')
numOpen = min(5, len(linkElms))
import pdb; pdb.set_trace()
for i in range(numOpen):
  webbrowser.open('http://google.com' + linkElms[i].get['href'])