CORRECTIVE_ACTIONS = {

    "OVERBILLING":
        "Adjust billed hours to match approved timesheet and trigger review.",

    "RATE_MISMATCH":
        "Correct billed rate to contractual rate and regenerate invoice.",

    "CONTRACT_HOURS_VIOLATION":
        "Escalate for contract exception approval or reduce hours.",

    "MISSING_BILLED_HOURS":
        "Review missing billed hours and reconcile timesheet entries.",

    "BILLING_AMOUNT_MISMATCH":
        "Recalculate invoice totals based on approved rates and hours."
}


def validate_row(row):

    issues=[]

    if row["Hours_Billed"] > row["Hours_Worked"]:
        issues.append("OVERBILLING")

    if row["Rate_Charged"] != row["Rate_per_Hour"]:
        issues.append("RATE_MISMATCH")

    if row["Hours_Worked"] > row["Max_Hours_Per_Week"]:
        issues.append(
            "CONTRACT_HOURS_VIOLATION"
        )

    if row["Hours_Billed"] < row["Hours_Worked"]:
        issues.append(
            "MISSING_BILLED_HOURS"
        )

    expected_amount=(
      row["Hours_Worked"] *
      row["Rate_per_Hour"]
    )

    billed_amount=(
      row["Hours_Billed"] *
      row["Rate_Charged"]
    )

    if expected_amount != billed_amount:
        issues.append(
          "BILLING_AMOUNT_MISMATCH"
        )


    if issues:
        corrective=[]

        for issue in issues:
            corrective.append(
               CORRECTIVE_ACTIONS[issue]
            )

        return (
           "ERROR",
           ",".join(issues),
           " | ".join(corrective)
        )

    return "OK","","No action required"



def run_validations(df):

    statuses=[]
    discrepancies=[]
    corrective_actions=[]

    for _,row in df.iterrows():

        status,issues,actions=validate_row(row)

        statuses.append(status)
        discrepancies.append(issues)
        corrective_actions.append(actions)

    df["Status"]=statuses
    df["Discrepancies"]=discrepancies
    df["Corrective_Actions"]=corrective_actions

    return df