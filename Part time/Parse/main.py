import pandas as pd
from bs4 import BeautifulSoup
import requests

items = []
url = 'https://www.luckyglass.com.ua/ua/catalog/'

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

all_items = soup.findAll('ul', class_='pagination pagination-large')
max_page=0
for _ in all_items:
    for a in _.findAll('a'):
        p_url = a.get('href')
        if p_url.find('?page=')>0:
            p_idx = int(p_url[p_url.find('?page=')+6:])
            if p_idx>max_page:
                max_page = p_idx

for p in range(1, max_page+1):
    if p!=1:
        r = requests.get(url+'?page='+str(p))
    print(r.status_code, url+'?page='+str(p))
    soup = BeautifulSoup(r.text, "html.parser")
    all_items = soup.findAll('div', class_='one-block')
    
    for i in all_items:
        item = {}
        for j in i.findAll('div', class_='vertical-middle-wrapper'):
            for _ in j.findAll('a'):
                item['link'] = url + _.get('href')
                item['name'] = _.text.strip()

        for j in i.findAll('div', class_='price'):            

            item['price'] = j.text.strip().replace(' грн', '')
            if j.get('style') is None:
                item['available'] = 1
            else:
                item['available'] = 0
                
                
                ##############################

        for j in i.findAll('div', class_='text-effect'):    

            start, stop = 0, 0
            _ = str(j)
            counter = 0
            while (stop<_.find('</div>')-6)and(counter<24):
                start = _[stop:].find('<b>')+3+stop
                stop = _[start:].find('</b>')+start

                k = (_[start:stop]).strip()
                start = _[stop:].find(':')+stop+1
                stop = _[start:].find('<br/>')+start
                v = (_[start:stop]).strip()
                item[k] = v
                counter+=1

        if len(item)>0:
            if '' in item.keys():
                item.pop('')
            items.append(item)

df = pd.DataFrame(data=items)
df.to_excel('luckyglass.xlsx', index=False)