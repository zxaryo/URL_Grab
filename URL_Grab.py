import urllib2
import re
import os
from os.path import basename
from urlparse import urlsplit
from urlparse import urlparse
from posixpath import basename,dirname
 
## function that processes url, if there are any spaces it replaces with '%20' ##
 
def process_url(raw_url):
 if ' ' not in raw_url[-1]:
     raw_url=raw_url.replace(' ','%20')
     return raw_url
 elif ' ' in raw_url[-1]:
     raw_url=raw_url[:-1]
     raw_url=raw_url.replace(' ','%20')
     return raw_url
 
url=raw_input("Enter URL: ") ## give the url here
parse_object=urlparse(url)
dirname=raw_input("DIR Name: ")
if not os.path.exists('images'):
    os.mkdir("images")
os.mkdir("images/"+dirname)
os.chdir("images/"+dirname)
z=urllib2.urlopen(url).read()
urlcontent=re.sub('\'','\"',z)
imgurls=re.findall('a .*?href="(.*?)"',urlcontent)
for imgurl in imgurls:
 try:
     print(imgurl)
     imgurl=process_url(imgurl)
     imgdata=urllib2.urlopen(imgurl).read()
     filname=basename(urlsplit(imgurl)[2])
     output=open(filname,'wb')
     output.write(imgdata)
     output.close()
     os.remove(filename)
 except:
     pass

