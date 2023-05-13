"""collect webpage result from query"""
import urllib, urllib.request
from bs4 import SoupStrainer, BeautifulSoup

def arxiv_search(search_term, start_idx=0, max_results=200, sort_by="relevance"):
    search_term = search_term.replace(" ", "%20")
    BASE_URL = "http://export.arxiv.org/api/query?search_query="
    
    assert(sort_by in ["relevance", "lastUpdatedDate", "submittedDate"])

    data = urllib.request.urlopen(f"{BASE_URL}" + search_term + f"&start={start_idx}" + f"&max_results={max_results}" + f"&sortBy={sort_by}")
    
    return data.read().decode('utf-8')

# https://stackoverflow.com/questions/13200709/extract-google-scholar-results-using-python-or-r
class GoogleScholarOpener(urllib.request.FancyURLopener):
    version = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36'

def googlescholar_search(search_term):
    openurl = GoogleScholarOpener().open
    unparsed = openurl(f"http://scholar.google.se/scholar?hl=en&q={search_term}").read()
    page = BeautifulSoup(unparsed, parse_only=SoupStrainer('div', id='gs_ab_md'), features="lxml")
    return page

if __name__ == "__main__":
    print(arxiv_search("deep learning", max_results=5, sort_by="lastUpdatedDate"))
    print(googlescholar_search("deep learning"))