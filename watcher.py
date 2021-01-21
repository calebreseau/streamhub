from googlesearch import search
from html.parser import HTMLParser
import requests
import json
import os.path
from os import path

DATA_SOURCES=['www.oxtorrent.cc','torhd.cc']
globals().update({'urls': []})


def cache_load(title):
    ret=[]
    with open('cache/'+title+'.cache','r') as f:
        lines=f.readlines()
        for line in lines:
            ret.append(line.split(','))
    return ret

def cache_save(title,ret):
    if not path.exists('cache'):
        os.mkdir('cache')
    with open('cache/'+title+'.cache', 'w') as f:
        for el in ret:
            f.write(','.join(el)+'\n')

def cache_get():
    ret=[]
    files=[]
    if path.exists('cache'):
        files=os.listdir('cache')
    for file in files:
        ret.append(file.replace('.cache',''))
    print('cache :')
    print(ret)
    return ret

def seek(title):
    ret=[]
    count=0
    if path.exists('cache/'+title+'.cache'):
        ret=cache_load(title)
    else:
        for site in DATA_SOURCES:
            urls=[]
            try:
                urls=search('"'+title+' torrent" site:'+site,num_results=2,lang='fr')
            except:
                return []
            parser=Parser()
            for url in urls:
                r=requests.get(url)
                parser.feed(str(r.content))
                for i in range(0,len(globals()['urls'])):
                    count+=1
                    ret.append([globals()['urls'][i],'#'+str(count)+': '+title+' from '+site])
        if len(ret)>0:
            cache_save(title,ret)
    return ret


class Parser(HTMLParser):

    def __init__(self):
            self.convert_charrefs = True
            self.reset()
            globals()['urls']=[]
            globals()['types']=[]


    def handle_starttag(self, tag, attrs):
        if tag=='a':
            _attrs={'href':''}
            for attr in attrs:
                _attrs[attr[0]]=str(attr[1]).replace('\\\'','')
            if 'magnet' in _attrs['href']:
                globals()['urls'].append(_attrs['href'])

    

