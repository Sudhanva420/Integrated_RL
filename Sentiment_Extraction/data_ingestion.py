import re
import requests
import pandas as pd
from langchain.document_loaders import UnstructuredPDFLoader

#This function extracts a quarter string like "2023Q1" from the filenames that were explicitly named in this fashion 
def extract_quarter_from_filename(filename):

    match = re.search(r'(\d{4}Q[1-4])', filename)
    return match.group(1) if match else None

#loads a report and is tagged with its quarter
def load_quarterly_report(pdf_path):
    loader = UnstructuredPDFLoader(pdf_path)
    docs = loader.load()
    text = "\n".join(d.page_content for d in docs)
    quarter = extract_quarter_from_filename(pdf_path)
    return {
        "text": text,
        "source": pdf_path,
        "type": "quarterly_report",
        "quarter": quarter
    }




