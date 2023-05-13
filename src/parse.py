"""Parse webpage result"""
from scrape import arxiv_search
from bs4 import BeautifulSoup
import json
from pprint import pprint

# # retunr list of dictionaries 

def res_to_dict(query:str) -> None:
  out = arxiv_search(query, max_results=5)
  pprint(out)
  docs = out.split("<entry>")
  pprint(docs[0])
  soup = BeautifulSoup(docs[0], "xml")
  # print(type(soup))
  pass
    
res_to_dict("deeplearning")

