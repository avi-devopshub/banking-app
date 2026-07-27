def pay_bill(biller, amount):
    if amount <= 0:
        return "Invalid Amount"

    return f"Paid ₹{amount} to {biller}"
