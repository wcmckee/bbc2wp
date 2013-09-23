# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# json data

# <codecell>

import requests
import json
import random
import time
import os
import pprint


# <headingcell level=2>

# BBC NEWS

# <codecell>

getTop = requests.get(u'http://api.bbcnews.appengine.co.uk/topics')
oldTop = json.loads(getTop.text)
#print oldTop

# <codecell>

woTop = random.randint(1,12)

# <codecell>

catTop = blaTop[woTop]
#print catTop

# <codecell>

idTop = catTop['id']
#print idTop

# <codecell>

urBbc = ('http://api.bbcnews.appengine.co.uk/stories/' + idTop)
#print urBbc
getBbc = requests.get(urBbc)
oldBbc = json.loads(getBbc.text)
#print oldBbc


# <codecell>

ehhBbc = oldBbc[u'topic'][u'title']
#print ehhBbc

# <codecell>

storBbc = oldBbc[u'stories']

# <codecell>

#print storBbc

# <codecell>

faiBbc = storBbc[0]
#print faiBbc

# <codecell>

thumBbc = faiBbc[u'thumbnail']

#print thumBbc

# <codecell>


titlBbc = faiBbc[u'title']
#print titlBbc

# <codecell>

desBbc = faiBbc[u'description']
#print desBbc

# <codecell>

linBbc = faiBbc['link']
#print linBbc

# <codecell>

pubBbc = faiBbc['published']

# <codecell>

#print pubBbc

# <codecell>

blaTop = oldTop['topics']
#print blaTop

couId = list.count(blaTop, "{")
#print couId

# <codecell>

savBbc = open('savBbc','w')
savBbc.write('<h1 style="text-align: center;"><strong>')
savBbc.write(ehhBbc)
savBbc.write('</strong></h1><h2 style="text-align: center;\"><a href=\"')
savBbc.write(linBbc)
savBbc.write('"><strong>')
savBbc.write(titlBbc)
savBbc.write('</strong></a></h2><p style="text-align: justify;">')
savBbc.write(desBbc)
savBbc.write('</p><img class="aligncenter" alt="" src="')
savBbc.write(thumBbc)
savBbc.write('" />')
savBbc.close()

tacBbc = open('tacBbc','w')
tacBbc.write(titlBbc)
tacBbc.close()

# <codecell>

opnBbc = ('savBbc','r')
for opn in opnBbc:
    print(opn)

# <codecell>

ls

# <codecell>


# <headingcell level=1>

# ArtControl, BroBeur, FreshFigure, WCMCKEE - json

# <codecell>

ranUrl = random.randint(0,3)
myUrl = ('artcontrol.me', 'freshfigure.com/art', 'brobeur.com', 'wcmckee.com')
fulUrl = myUrl[ranUrl]
#print fulUrl

# <codecell>

comUrl = ('http://' + fulUrl + '/?wpapi=get_posts&dev=0')
#print comUrl

# <codecell>

getArt = requests.get(comUrl)
oldArt = json.loads(getArt.text)
#print oldBbc
anoArt = oldArt[u'posts']
#print anoArt

titArt = anoArt[0]
#print titArt

# <codecell>

exArt = titArt[u'excerpt']

# <codecell>

#print exArt

# <codecell>

namArt = titArt[u'title']
#print namArt


# <codecell>


# <codecell>


# <codecell>

urlArt = titArt[u'url']
#print urlArt

# <codecell>

datArt = titArt[u'date']
#print datArt

# <codecell>

sluArt = titArt['slug']
#print sluArt

# <codecell>

parArt = titArt['parent']
#print parArt

# <codecell>

savFile = open('savFile','w')
savFile.write(namArt)
savFile.write(' - ')
savFile.write(exArt)
savFile.write(datArt)
savFile.close()

# <codecell>

opeFile = open('savFile','r')
for file in opeFile:
     print(file)

# <codecell>

n = random.randint(1,20)
#print n

# <codecell>

timNum = random.randint(1,12)
#print timNum

# <codecell>

x = timNum * n
#print x

# <codecell>

lisNum = [n, timNum, x]
#print lisNum

# <codecell>

derbNum = list.sort(lisNum)
#print derbNum

# <codecell>

#print lisNum

