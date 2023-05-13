"""Rank model"""

import cohere
import requests
import numpy as np
from time import time
from typing import List
import parse
import pandas as pd
import json
import os
import io
import anthropic
import PyPDF2

# Set up your cohere client
API_KEY = "ROZ1XaiS9AgwHygUhXRK6xhDbxQXroQ9xURzqxFE"
co = cohere.Client(API_KEY)

client = anthropic.Client('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')

# Example query and passages (data taken from http://sbert.net/datasets/simplewiki-2020-11-01.jsonl.gz)
print("What can we help you find?")
query = str(input())
arxis_docs = parse.arxiv_parsing(query)

results = co.rerank(query=query, documents=arxis_docs, top_n=3, model='rerank-english-v2.0') # Change top_n to change the number of results returned. If top_n is not passed, all results will be returned.
best_article_index = 100
for idx, r in enumerate(results):
  print(f"Document Rank: {idx + 1}, ArXiv Relevancy Index: {r.index}")
  print(f"Document: {r.document['text']}")
  print(f"Relevance Score: {r.relevance_score:.2f}")
  print("\n")
  if r.index < best_article_index:
    best_article_index = r.index

url = arxis_docs[list(arxis_docs)[best_article_index]]["pdf_url"]

r = requests.get(url)
f = io.BytesIO(r.content)

reader = PyPDF2.PdfReader(f)

contents = ""

for i in range(len(reader.pages)):
    page_contents = reader.pages[i].extract_text()
    contents += page_contents + " "

summary_prompt = f"{anthropic.HUMAN_PROMPT} Teach me how this {contents} works by asking questions about my level of understanding \
  of necessary concepts. With each response, fill in gaps in my understanding, then recursively ask me more \
  questions to check my understanding. Identify and share the most important 20% of learnings from this paper \
  that will help me understand 80% of it. {anthropic.AI_PROMPT}"

response = client.completion(
    prompt= summary_prompt,
    stop_sequences = [anthropic.HUMAN_PROMPT],
    model="claude-v1-100k",
    max_tokens_to_sample=5000,
)
print(response['completion'])
