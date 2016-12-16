# _*_ coding: utf-8 _*_
# author: guoxiaopolu

import urllib2
import urllib
from BeautifulSoup import *

pages = []

# Get all the links that contain Xiliang photos
for i in range(1, 11):
	pages.append('http://www.fatieku.net/postcache/2014/07/27/b-skcxak/page-%s.html' % i)

# Get links to all photos
def get_photo_url(pages):
	photourl = []

	for page in pages:
		headers = {'User-Agent':'Mozilla/5.0 (X11; U; Linux i686)Gecko/20071127 Firefox/2.0.0.11'}
		req = urllib2.Request(url = page, headers = headers)
		c = urllib2.urlopen(req)

		content = c.read()

		soup = BeautifulSoup(content)

		imgs = soup.findAll('img')

		for img in imgs:
			tempdict = dict(img.attrs)
			if 'onload' in tempdict:
				imgload = tempdict['onload']

				imgpath = imgload.split(',')[1]

				photourl.append(imgpath[1:-1])

	return photourl

# Download all photos from all specified paths
def download_from_url(photourl):

	for i, url in enumerate(photourl):
		urllib.urlretrieve(url, '/home/guoxiaopolu/xiliangphoto/xiliang%s.jpg' % i)

# Get it
if __name__ == '__main__':
	photourl = get_photo_url(pages)
	download_from_url(photourl)