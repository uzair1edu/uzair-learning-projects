# auto_ticket_classifier.py
# Very simple rule-based ticket classifier (demo)

def classify_ticket(text):
    text = text.lower()
    if "refund" in text or "charge" in text:
        return "Billing"
    if "login" in text or "password" in text:
        return "Login/Account"
    if "deliver" in text or "shipping" in text:
        return "Delivery"
    return "General"

# demo
examples = [
    "I want a refund for my order",
    "I can't login to my account",
    "Where is my delivery?"
]

for e in examples:
    print(e, "->", classify_ticket(e))
