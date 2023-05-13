import streamlit as st
# from PIL import Image
# import numpy as np
from src.rank import document_search_and_ranking, summarize_document

# img = np.array(Image.open('logo.png'))
# st.image(image=img, caption="InstantResearch.AI")

st.title("InstantResearch.AI")
IGNORED_KEYS = ["published", "updated", "rank"]

with st.form(key='query_form'):
	query = st.text_input(label='search academia')
	query_submit = st.form_submit_button(label='Submit')

with st.form(key="summary_form"):
	doc_url = st.text_input(label='Summarize a pdf article! (provide url link to pdf)', help="provide a url link to the desired pdf")
	summary_submit = st.form_submit_button(label='Submit')

placeholder = st.empty()

if query_submit: # process 
  placeholder = st.empty()
  with placeholder.container():
    docs = document_search_and_ranking(query)
    for i, (doc_id, v) in enumerate(docs.items()):
      st.markdown(body=f"## #{i} arxiv doc_id: {doc_id}")
      for doc_k, doc_v in v.items():
        if doc_k not in IGNORED_KEYS:
          st.markdown(body=f"### {doc_k}")
          st.markdown(body=f"{doc_v}")
      st.divider()

if summary_submit:
  placeholder = st.empty()
  with placeholder.container():
      pdf_summary = summarize_document(doc_url)
      st.markdown(body=pdf_summary)