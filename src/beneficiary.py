def add_beneficiary(name, account_number, ifsc):
    if not name or not account_number or not ifsc:
        return "Invalid Beneficiary Details"

    return f"Beneficiary {name} added successfully"
