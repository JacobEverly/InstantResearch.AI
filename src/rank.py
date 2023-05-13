"""Rank model"""

import cohere
import requests
import numpy as np
from time import time
from typing import List
import parse
import pandas as pd
import json

# Set up your cohere client
API_KEY = "ROZ1XaiS9AgwHygUhXRK6xhDbxQXroQ9xURzqxFE"
co = cohere.Client(API_KEY)

# Example query and passages (data taken from http://sbert.net/datasets/simplewiki-2020-11-01.jsonl.gz)
query = str(input())
arxis_docs = parse.arxiv_parsing(query)

results = co.rerank(query=query, documents=arxis_docs, top_n=3, model='rerank-english-v2.0') # Change top_n to change the number of results returned. If top_n is not passed, all results will be returned.
for idx, r in enumerate(results):
  print(f"Document Rank: {idx + 1}, ArXiv Relevancy Index: {r.index}")
  print(f"Document: {r.document['text']}")
  print(f"Relevance Score: {r.relevance_score:.2f}")
  print("\n")
