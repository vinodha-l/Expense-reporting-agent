# Expense Reporting AI Environment

## Description
This is a real-world simulation of an expense auditing task. An AI agent must look at digital receipts and verify the total amounts against a database.

## Requirements
- **Goal**: Verify receipt amounts with 100% accuracy.
- **Tasks**: 
  1. Easy: Single receipt verification.
  2. Medium: Multiple receipt matching.
  3. Hard: Fraud detection (identifying mismatching dates).

## Technical Details
- **Action Space**: `type(target, value)`, `click(target)`.
- **Observation Space**: Text-based receipt data and screenshots.
- **API**: Standard `step()`, `reset()`, and `state` models.

## How to Run
Built using Docker. Use `docker build -t expense-env .` to initialize.