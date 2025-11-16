# sentiment_detector.py
# Simple polarity check using keywords (offline demo)

def sentiment(text):
    text = text.lower()
    positives = ["good","great","happy","satisfied"]
    negatives = ["bad","angry","unhappy","unsatisfied","complaint"]
    score = sum(1 for w in positives if w in text) - sum(1 for w in negatives if w in text)
    return "Positive" if score>0 else ("Negative" if score<0 else "Neutral")

# demo
print(sentiment("I am very unsatisfied with this product"))
print(sentiment("Delivery was great and I am happy"))
