import anthropic
from dotenv import load_dotenv
import os

load_dotenv()  # reads your .env file
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def ask(prompt):
    msg = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )
    return msg.content[0].text

def classify_ticket(ticket):
    prompt = f"""You are a customer support triage assistant.
Classify this ticket. Return exactly these 4 lines:
Category: (billing / technical / complaint / other)
Sentiment: (one word)
Escalate to human: (yes/no)
Reason: (one short sentence)

Ticket: {ticket}"""
    return ask(prompt)

tickets = [
    "I was charged twice and no one has replied in 3 days.",
    "How do I export my data to CSV?",
    "Your service is terrible and I'm cancelling."
]

for t in tickets:
    print("TICKET:", t)
    print(classify_ticket(t))
    print("-" * 40)