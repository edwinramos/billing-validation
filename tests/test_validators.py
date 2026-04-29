from src.validators import validate_row


def test_overbilling_flagged():

    row = {
        "Hours_Billed":50,
        "Hours_Worked":40,
        "Rate_Charged":20,
        "Rate_per_Hour":20,
        "Max_Hours_Per_Week":45
    }

    status,issues,actions = validate_row(row)

    assert status == "ERROR"
    assert "OVERBILLING" in issues
    assert "Adjust billed hours" in actions



def test_rate_mismatch_flagged():

    row = {
        "Hours_Billed":40,
        "Hours_Worked":40,
        "Rate_Charged":25,
        "Rate_per_Hour":20,
        "Max_Hours_Per_Week":45
    }

    status,issues,actions = validate_row(row)

    assert status=="ERROR"
    assert "RATE_MISMATCH" in issues
    assert "Correct billed rate" in actions



def test_contract_violation_flagged():

    row = {
        "Hours_Billed":45,
        "Hours_Worked":45,
        "Rate_Charged":30,
        "Rate_per_Hour":30,
        "Max_Hours_Per_Week":40
    }

    status,issues,actions = validate_row(row)

    assert status=="ERROR"
    assert "CONTRACT_HOURS_VIOLATION" in issues



def test_clean_record_ok():

    row = {
        "Hours_Billed":40,
        "Hours_Worked":40,
        "Rate_Charged":20,
        "Rate_per_Hour":20,
        "Max_Hours_Per_Week":40
    }

    status,issues,actions = validate_row(row)

    assert status=="OK"
    assert issues==""