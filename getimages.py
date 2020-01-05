import os, fnmatch, requests, time, webbrowser
from pathlib import Path
from bs4 import BeautifulSoup
import urllib.request
path = Path()
num = input("How many glyphs: ")
i = 13314
for z in range(int(num)):
	q = str(hex(i+z))[2:]
	response = requests.get("http://en.glyphwiki.org/glyph/u" + q + "@4.50px.png")
	try:
		urllib.request.urlretrieve("http://en.glyphwiki.org/glyph/u" + q + "@4.50px.png","glyhp_" + str(z) + ".png")
		print("Downloaded glyhp №" + str(z+1))
	except urllib.error.HTTPError as e:
   		if e.code == 404:
   			print("Passing glyph " + str(hex(i+z)[2:]))
   			z -= 1