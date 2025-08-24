import re
from transformers import pipeline, AutoTokenizer
from collections import Counter

def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip()

model_id = "/content/drive/MyDrive/RL_Project/finbert_kdave_trained/finbert_kdave_trained"
finbert = pipeline("sentiment-analysis", model=model_id)
tokenizer = AutoTokenizer.from_pretrained(model_id)

def split_text_into_chunks(text, max_tokens=512):
    tokens = tokenizer.tokenize(text)
    chunk_size = max_tokens - 2
    chunks = []
    for i in range(0, len(tokens), chunk_size):
        chunk_tokens = tokens[i:i+chunk_size]
        chunks.append(tokenizer.convert_tokens_to_string(chunk_tokens))
    return chunks
#Retrieves the sentiment label and score for each chunk using our fine-tuned FinBERT
def get_sentiment(text):
    text = clean_text(text)
    tokens = tokenizer.tokenize(text)
    if len(tokens) <= 510:
        res = finbert(text, truncation=True, max_length=512)
        return res[0]['label'], res[0]['score']
    chunks = split_text_into_chunks(text)
    labels, scores = [], []
    for c in chunks:
        if not c.strip(): continue
        res = finbert(c, truncation=True, max_length=512)
        labels.append(res[0]['label']); scores.append(res[0]['score'])
    if not scores: return None, None
    label = Counter(labels).most_common(1)[0][0]
    return label, sum(scores) / len(scores)
#Assigning sentiment for each document
def sentiment_chain(doc):
    label, score = get_sentiment(doc["text"])
    return {
        "quarter": doc["quarter"],
        "sentiment_label": label,
        "sentiment_score": score
    }


