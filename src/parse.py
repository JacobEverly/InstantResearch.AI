"""Parse webpage result"""
from src.scrape import arxiv_search
import re
import io
import requests
import PyPDF2


def arxiv_parsing(query: str) -> None:
    out = arxiv_search(query)
    # print(out)
    # pprint(out)
    docs = out.split("<entry>")[1:]

    results = {}  # arxiv ID -> {dict mapping of a bunch of fields}
    for doc in docs:
        arxiv_id = (
            doc.split("<id>")[1].split("</id>")[0].split("http://arxiv.org/abs/")[1]
        )
        results[arxiv_id] = {}

        results[arxiv_id]["updated"] = doc.split("<updated>")[1].split("</updated>")[0]
        results[arxiv_id]["published"] = doc.split("<published>")[1].split(
            "</published>"
        )[0]
        results[arxiv_id]["title"] = doc.split("<title>")[1].split("</title>")[0]
        results[arxiv_id]["summary"] = doc.split("<summary>")[1].split("</summary>")[0]
        results[arxiv_id]["url"] = doc.split("<id>")[1].split("</id>")[0]
        results[arxiv_id]["authors"] = re.findall(r"<name>(.+?)</name>", doc)
        results[arxiv_id]["pdf_url"] = doc.split('<link title="pdf" href="')[1].split(
            '" rel="related" type="application/pdf"/>'
        )[0]

    return results


def arxiv_pdf_parsing(url):
    r = requests.get(url)
    f = io.BytesIO(r.content)

    reader = PyPDF2.PdfReader(f)

    contents = ""

    for i in range(len(reader.pages)):
        page_contents = reader.pages[i].extract_text()
        contents += page_contents + " "

    return contents


if __name__ == "__main__":
    results = arxiv_parsing("deep learning")

    url = results[list(results)[0]]["pdf_url"]

    print(url)

    contents = arxiv_pdf_parsing(url)

    print(contents)  # this is the full pdf contents
