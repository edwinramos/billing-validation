# Billing Validation Prototype

## Objective
Prototype to detect billing discrepancies before invoices are sent to clients.

This solution identifies:

- Overbilling
- Rate mismatches
- Contract hour violations
- Billing amount discrepancies

It generates:

- Validation flags (OK / ERROR)
- Corrective actions
- AI-style discrepancy explanations
- Final audit output


---

## Tech Stack

- Python
- Pandas
- Pytest
- Streamlit (optional)
- Deterministic AI reasoning layer


---

## Repository Structure

/data
Input datasets

/src
Core processing scripts

/tests
Validation tests

/prompts
Prompt templates for AI reasoning

/workflows
Workflow documentation

/output
Generated audit reports


---

## Business Rules

### Overbilling
Hours Billed > Hours Worked

### Rate Mismatch
Charged Rate != Contract Rate

### Contract Violation
Worked Hours > Max_Hours_Per_Week

### Billing Amount Mismatch
Calculated bill != Actual bill


---

## Solution Architecture

Hybrid discrepancy engine:

1 Rule-based deterministic validation

2 Corrective action recommendation mapping

3 AI reasoning layer (with deterministic fallback)


This separates audit controls from AI explanation generation.


---

## Run Instructions

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
cd src
python main.py
```

Run tests:

```bash
pytest
```


---

## Output
Generated report:

output/billing_audit.csv


---

## Governance Considerations

- Deterministic rules drive audit decisions
- AI is used only for explanation support
- Corrective recommendations are auditable
- Human review required before invoice correction


---

## Future Enhancements

- Streamlit review dashboard
- API deployment
- Automated workflow scheduling
- LLM-powered anomaly detection
