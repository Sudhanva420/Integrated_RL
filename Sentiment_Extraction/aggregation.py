# aggregation.py
import numpy as np
from collections import defaultdict

def aggregate_quarterly_sentiments(results):
    
    buckets = defaultdict(list)
    for r in results:
        q, s = r.get("quarter"), r.get("sentiment_score")
        if q and s is not None:
            buckets[q].append(s)
    return {q: float(np.mean(scores)) for q, scores in buckets.items()}

