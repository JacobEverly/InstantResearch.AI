import streamlit as st
# from PIL import Image
# import numpy as np
from src.rank import document_search_and_ranking, summarize_document

# img = np.array(Image.open('logo.png'))
# st.image(image=img, caption="InstantResearch.AI")

st.title("InstantResearch.AI")
IGNORED_KEYS = ["published", "updated", "rank", "url"]

with st.form(key='context_form'):
  context = st.text_input(label='What is your area of research?')
  context_submit = st.form_submit_button(label='Enter')

with st.form(key='query_form'):
	query = st.text_input(label='What do you want to learn?')
	query_submit = st.form_submit_button(label='Submit')

with st.form(key="summary_form"):
	doc_url = st.text_input(label='Summarize a pdf article! (provide url link to pdf)', help="provide a url link to the desired pdf")
	summary_submit = st.form_submit_button(label='Submit')

placeholder = st.empty()

if query_submit: # process 
  placeholder = st.empty()
  with placeholder.container():
    context_prompt = None
    if context_submit:
       context_prompt = context
    docs = document_search_and_ranking(context, query)
    for i, (doc_id, v) in enumerate(docs.items()):
      st.markdown(body=f"## #{i+1}")
      for doc_k, doc_v in v.items():

        if doc_k not in IGNORED_KEYS:
          doc_k = doc_k.capitalize()
          
          if doc_k != 'Summary':
            st.markdown(body=f"### {doc_k}")
          else:
             st.markdown(body="### Abstract")
          
          if doc_k != "Authors":
            st.markdown(body=f"{doc_v}")
          else:
            st.markdown(body=", ".join(doc_v))

      st.divider()

if summary_submit:
  placeholder = st.empty()
  with placeholder.container():
    try:
      pdf_summary = summarize_document(doc_url)
      st.markdown(body=pdf_summary)
    except:
       st.markdown(body="## :red[not a valid pdf!]")