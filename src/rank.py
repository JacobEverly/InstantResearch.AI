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

API_KEY = "ROZ1XaiS9AgwHygUhXRK6xhDbxQXroQ9xURzqxFE"
co = cohere.Client(API_KEY)

client = anthropic.Client('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')

def document_search_and_ranking(first_query):
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

    arxiv_docs = parse.arxiv_parsing(second_query)

    results = co.rerank(query=second_query, documents=arxiv_docs, top_n=5, model='rerank-english-v2.0') # Change top_n to change the number of results returned. If top_n is not passed, all results will be returned.

    document_results = {}

    for idx, r in enumerate(results):
      #print(f"Document Rank: {idx + 1}, ArXiv Relevancy Index: {r.index}")
      #print(f"Document: {r.document['text']}")
      #print('Title: ' + str(arxiv_docs[list(arxiv_docs)[idx]]["title"]))
      # print(f"Relevance Score: {r.relevance_score:.2f}")
      #print("\n")
      # extract the document information for the relevant documents
      document_results[r.document['text']] = arxiv_docs[list(arxiv_docs)[idx]]
      document_results[r.document['text']]["rank"] = idx + 1
      document_results[r.document['text']]["arxiv_relevancy_score"] = r.index

    return document_results

def summarize_document(document_url):
    contents = parse.arxiv_pdf_parsing(document_url)

    summary_prompt = f"{anthropic.HUMAN_PROMPT} Teach me about this paper {contents}. Identify and share the most important \
      20% of learnings from this paper that will help me understand 80% of it. I want the reply to this prompt to only be the summary. \
      The summary should be formatted as numbered sections, with bold headings for each section. \
      In each section there should be the summary of what is needed to be known to make sure I have the 80% understanding of the paper. {anthropic.AI_PROMPT}"

    response = client.completion(
        prompt= summary_prompt,
        stop_sequences = [anthropic.HUMAN_PROMPT],
        model="claude-v1-100k",
        max_tokens_to_sample=5000,
    )

    return response['completion']

if __name__ == "__main__":
    print("What can we help you find?")
    first_query = str(input())

    document_results = document_search_and_ranking(first_query)

    for i, d in enumerate(document_results.values()):
        print("Title:", d["title"])
        print("Authors:", ", ".join(d["authors"]))
        print("Cohere Rank:", d["rank"])
        print("Arxiv Rank:", d["arxiv_relevancy_score"])
        print("")

    print('Which document would you like summarized?')
    which_summary = int(input())

    document_url = document_results[list(document_results)[which_summary]]["pdf_url"]

    summary = summarize_document(document_url)

    print("Document url:", document_url)
    print(summary)
