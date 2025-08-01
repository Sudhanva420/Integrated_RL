# data_ingestion.py
import re
import requests
import pandas as pd
from langchain.document_loaders import UnstructuredPDFLoader

def extract_quarter_from_filename(filename):
    """
    Extracts a quarter string (e.g., "2023Q1") from a filename.
    Expects filenames like 'INFY_2023Q2_report1.pdf'.
    """
    match = re.search(r'(\d{4}Q[1-4])', filename)
    return match.group(1) if match else None

def load_quarterly_report(pdf_path):
    """
    Loads a PDF quarterly report, concatenates its text, and tags it with its quarter.
    """
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
