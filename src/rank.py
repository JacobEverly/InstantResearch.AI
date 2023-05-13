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

print("What can we help you find?")
first_query = str(input())

# Example query and passages (data taken from http://sbert.net/datasets/simplewiki-2020-11-01.jsonl.gz)
summary_prompt = f"{anthropic.HUMAN_PROMPT} You are an expert in the {first_query}. I want to conduct \
  an inclusive search in an Academic database for papers to figure out “What you want to learn”. Provide me \
    with the best search criteria to use with the database to find papers relevant to my topic. The suggested \
      search should try to be as inclusive as possible to result in the most papers possible on the topic. I \
        want the only response to this message to be what I should put in the search bar.  {anthropic.AI_PROMPT}"

response = client.completion(
    prompt= summary_prompt,
    stop_sequences = [anthropic.HUMAN_PROMPT],
    model="claude-v1-100k",
    max_tokens_to_sample=5000,
)

second_query = response['completion']

arxis_docs = parse.arxiv_parsing(second_query)

results = co.rerank(query=second_query, documents=arxis_docs, top_n=5, model='rerank-english-v2.0') # Change top_n to change the number of results returned. If top_n is not passed, all results will be returned.

for idx, r in enumerate(results):
  print(f"Document Rank: {idx + 1}, ArXiv Relevancy Index: {r.index}")
  print(f"Document: {r.document['text']}")
  print('Title: ' + str(arxis_docs[list(arxis_docs)[idx]]["title"]))
  # print(f"Relevance Score: {r.relevance_score:.2f}")
  print("\n")

print('Which document would you like summarized?')
which_summary = int(input())

url = arxis_docs[list(arxis_docs)[which_summary]]["pdf_url"]
contents = parse.arxiv_pdf_parsing(url)

summary_prompt = f"{anthropic.HUMAN_PROMPT} Teach me how this {contents} works by asking questions about my level of understanding \
  of necessary concepts. Identify and share the most important 20% of learnings from this paper \
  that will help me understand 80% of it. After summarizing the article, do not add any other text. {anthropic.AI_PROMPT}"

response = client.completion(
    prompt= summary_prompt,
    stop_sequences = [anthropic.HUMAN_PROMPT],
    model="claude-v1-100k",
    max_tokens_to_sample=5000,
)
print(response['completion'])
print('Source: ' + str(url))
