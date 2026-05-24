# Support Ticket Triage Agent

An AI agent that classifies incoming customer support tickets by category,
sentiment, and urgency — and flags which ones need a human.

## The problem
Support teams drown in tickets. Routing them manually is slow and
inconsistent. This prototype triages a ticket the way an experienced
support agent would, in seconds.

## What it does
- Classifies each ticket: billing / technical / complaint / other
- Detects sentiment
- Decides whether to escalate to a human (and why)

## How it works
Built with the Anthropic Claude API. Each ticket is passed through a
structured prompt that returns a consistent, parseable triage output.

## Why I built it
I led customer-experience solution engineering teams for ~10 years.
I built this to understand agentic CX from the deployer's side — how
these systems are actually designed, not just sold.

## Tech
Python · Anthropic Claude API · Google Colab

## Next steps
- Add customer-history lookup (tool use)
- Add guardrails for out-of-scope requests
- Add an eval harness to measure accuracy across test cases
