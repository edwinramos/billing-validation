import os
from dotenv import load_dotenv

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")


# Initialize client only if key exists
client = None

if OPENAI_AVAILABLE and api_key:
    client = OpenAI(
        api_key=api_key
    )


def local_fallback_explanation(row):

    issues = row["Discrepancies"]

    explanations=[]
    actions=[]


    if "OVERBILLING" in issues:

        explanations.append(
            "Billed hours exceed approved worked hours."
        )

        actions.append(
            "Adjust invoice hours and trigger supervisor review."
        )


    if "RATE_MISMATCH" in issues:

        explanations.append(
            "Charged rate differs from contract rate."
        )

        actions.append(
            "Correct billing rate and recalculate invoice."
        )


    if "CONTRACT_HOURS_VIOLATION" in issues:

        explanations.append(
            "Worked hours exceed contractual limits."
        )

        actions.append(
            "Escalate for contract exception approval."
        )


    if "MISSING_BILLED_HOURS" in issues:

        explanations.append(
            "Worked hours were not fully billed."
        )

        actions.append(
            "Reconcile timesheet and billing entries."
        )


    if "BILLING_AMOUNT_MISMATCH" in issues:

        explanations.append(
            "Invoice amount does not match approved calculation."
        )

        actions.append(
            "Recalculate billing totals."
        )


    if not explanations:

        return """
No discrepancies detected.

Suggested Action:
No corrective action required.
"""


    return f"""
Root Cause:
{' '.join(explanations)}

Suggested Corrective Actions:
{' '.join(actions)}

Generated via deterministic fallback reasoning.
"""



def generate_ai_explanation(row):


    if row["Status"]=="OK":
        return """
No discrepancies detected.

Suggested Action:
No correction required.
"""


    # If no client configured, use fallback
    if client is None:
        return local_fallback_explanation(
            row
        )


    try:

        prompt=f"""
You are a billing audit assistant.

Analyze:

Employee:
{row["Employee_Name"]}

Project:
{row["Project"]}

Hours Worked:
{row["Hours_Worked"]}

Hours Billed:
{row["Hours_Billed"]}

Contract Rate:
{row["Rate_per_Hour"]}

Charged Rate:
{row["Rate_Charged"]}

Detected Issues:
{row["Discrepancies"]}

Provide:

1 Root cause

2 Risks

3 Corrective actions

Be concise and audit-oriented.
"""


        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role":"user",
                    "content":prompt
                }
            ],
            temperature=0.2
        )


        return response.choices[0].message.content


    except Exception as e:

        print(
            f"OpenAI unavailable. Using fallback: {e}"
        )

        return local_fallback_explanation(
            row
        )