import pandas as pd


def load_data():

    timesheet = pd.read_csv("../data/timesheet.csv")
    billing = pd.read_csv("../data/billing.csv")
    contracts = pd.read_csv("../data/contracts.csv")

    df = (
        timesheet
        .merge(
            billing,
            on=["Employee_ID","Project"]
        )
        .merge(
            contracts,
            on="Project"
        )
    )

    return df