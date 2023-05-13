"""Parse webpage result"""
from scrape import arxiv_search
from bs4 import BeautifulSoup
import json
from pprint import pprint
import re

def arxiv_parsing(query:str) -> None:
    out = arxiv_search(query, max_results=5)
    #print(out)
    #pprint(out)
    docs = out.split("<entry>")[1:]

    results = {} # arxiv ID -> {dict mapping of a bunch of fields}
    for doc in docs:
        arxiv_id = doc.split("<id>")[1].split("</id>")[0].split("http://arxiv.org/abs/")[1]
        results[arxiv_id] = {}

        results[arxiv_id]["updated"] = doc.split("<updated>")[1].split("</updated>")[0]
        results[arxiv_id]["published"] = doc.split("<published>")[1].split("</published>")[0]
        results[arxiv_id]["title"] = doc.split("<title>")[1].split("</title>")[0]
        results[arxiv_id]["summary"] = doc.split("<summary>")[1].split("</summary>")[0]
        results[arxiv_id]["url"] = doc.split("<id>")[1].split("</id>")[0]

        results[arxiv_id]["authors"] = re.findall(r'<name>(.+?)</name>', doc)

    return results

if __name__ == "__main__":
    print(arxiv_parsing("deep learning"))
    
