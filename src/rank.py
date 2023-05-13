"""Rank model"""

import cohere
import requests
import numpy as np
from time import time
from typing import List
from pprint import pprint
import parse

# Set up your cohere client
API_KEY = "ROZ1XaiS9AgwHygUhXRK6xhDbxQXroQ9xURzqxFE"
co = cohere.Client(API_KEY)

# Example query and passages (data taken from http://sbert.net/datasets/simplewiki-2020-11-01.jsonl.gz)

query = str(input())
docs = [
    "Carson City is the capital city of the American state of Nevada. At the 2010 United States Census, Carson City had a population of 55,274.",
    "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean that are a political division controlled by the United States. Its capital is Saipan.",
    "Charlotte Amalie is the capital and largest city of the United States Virgin Islands. It has about 20,000 people. The city is on the island of Saint Thomas.",
    "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district. The President of the USA and many major national government offices are in the territory. This makes it the political center of the United States of America.",
    "West Virginia is a state in the Appalachian region of the United States. Its capital and largest city is Charleston. It is often abbreviated W. Va. or simply WV.",
    "Capital punishment (the death penalty) has existed in the United States since before the United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states. The federal government (including the United States military) also uses capital punishment.",
    "North Dakota is a state in the United States. 672,591 people lived in North Dakota in the year 2010. The capital and seat of government is Bismarck.",
    "Kentucky is a state in the United States. Its capital is Frankfort. It touches the states of Missouri (by the Mississippi River), Illinois, Indiana, Ohio, West Virginia (by the Ohio River), Tennessee and Virginia. There are many rivers in Kentucky",
    "Micronesia, officially the Federated States of Micronesia, is an island nation in the Pacific Ocean, northeast of Papua New Guinea. The country is a sovereign state in free association with the United States. The capital city of Federated States of Micronesia is Palikir.",
    "Utah is a state in the west United States. The capital and largest city is Salt Lake City. Utah became a state in the U.S. on January 4, 1896."]

results = co.rerank(query=query, documents=docs, top_n=3, model='rerank-english-v2.0') # Change top_n to change the number of results returned. If top_n is not passed, all results will be returned.
for idx, r in enumerate(results):
  print(f"Document Rank: {idx + 1}, Document Index: {r.index}")
  print(f"Document: {r.document['text']}")
  print(f"Relevance Score: {r.relevance_score:.2f}")
  print("\n")