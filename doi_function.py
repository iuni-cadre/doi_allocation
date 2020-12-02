#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 10:50:11 2020

@author: maahutch
"""
import requests
from requests.auth import HTTPBasicAuth
import json
from datetime import date 


with open('pwd.json') as f:
  data = json.load(f)


#Create draft DOI
def create_draft_doi(creator, title, contentUrl, cred): 

    headers = {'content-type': 'application/vnd.api+json'}
    
    create_date = date.today()
    
    metadata = {"data": {"type": "dois",
                        "attributes": {"prefix": "10.26313",
                                       "publisher": "Cadre",
                                       "publicationYear": str(create_date.year),                        
                                       "contenturl": contentUrl,
                                       "creators": [{
                                                     "name": creator
                                                     }],
                                       "titles": [{
                                                   "title": title
                                                   }],
                                       "created": str(create_date), 
                                       "types":{
                                                 "resourceTypeGeneral":"Software"
                                               }
                                       }}}
    payload = json.dumps(metadata, indent = 4)
    
    url = 'https://api.datacite.org/dois'
    
    
    response = requests.request("POST", url, data = payload,  headers=headers, auth = HTTPBasicAuth(cred['Username'], cred['Password']))
    
    return(response.text)
    
#Call function 
#create_draft_doi(creator= creator, title=title, contentUrl=contentUrl, cred=data)


#Converts draft DOI to findable DOI, requires that DOI already exists
#Not tested since I didn't want to create a permenant DOI
def create_findable_doi(doi, creator, title, contentUrl, cred): 

    headers = {'content-type': 'application/vnd.api+json'}
    
    create_date = date.today()
    
    metadata = {"data": {"type": "dois",
                        "attributes": {"doi": doi,
                                       "publisher": "Cadre",
                                       "publicationYear": str(create_date.year),                        
                                       "contenturl": contentUrl,
                                       "creators": [{
                                                     "name": creator
                                                     }],
                                       "titles": [{
                                                   "title": title
                                                   }],
                                       "created": str(create_date), 
                                       "types":{
                                                 "resourceTypeGeneral":"Software"
                                               },
                                       "event": "publish"
                                       }}}
    payload = json.dumps(metadata, indent = 4)
    
    url = 'https://api.datacite.org/dois'
     
    response = requests.request("POST", url, data = payload,  headers=headers, auth = HTTPBasicAuth(cred['Username'], cred['Password']))
    
    return(response.text)