def transfer(from_account, to_account, amount):
    if amount <= 0:
        return "Invalid Amount"

    return f"Transferred ₹{amount} from {from_account} to {to_account}"
