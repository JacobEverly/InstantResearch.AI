"""collect webpage result from query"""
import requests
import urllib, urllib.request

def arxiv_search(search_term, start_idx=0, max_results=200, sort_by="relevance"):
    search_term = search_term.replace(" ", "%20")
    BASE_URL = "http://export.arxiv.org/api/query?search_query="
    
    assert(sort_by in ["relevance", "lastUpdatedDate", "submittedDate"])

    data = urllib.request.urlopen(f"{BASE_URL}" + search_term + f"&start={start_idx}" + f"&max_results={max_results}" + f"&sortBy={sort_by}")
    
    return data.read().decode('utf-8')

def googlescholar_search(search_term):
    pass


if __name__ == "__main__":
    print(arxiv_search("deep learning", max_results=5, sort_by="lastUpdatedDate"))
