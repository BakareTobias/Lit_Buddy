import json
import requests

keyword = 'machine learning'
springer_key = '8acabdf7c7db9349af44366e28f722e1'



url = f"https://api.springernature.com/meta/v2/json?q={keyword}&api_key={springer_key}&s=1&p=2"

response = requests.get(url)
data = (response.json())

#data
    #apiMessage
    #query
    #result
    #records-> abstract
    #facets
title = data['records']
abstract = data['records'][1]['abstract']

for i,item in enumerate(data['records']):
    print({
        f'{i}':[item['title'],item['abstract'],item['doi'],item['url'][0]['value']]
        })
    print()