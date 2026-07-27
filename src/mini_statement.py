def get_mini_statement(transactions):
    if not transactions:
        return []

    # Show the latest five transactions
    return transactions[-5:]


def get_transaction_history(transactions):
    if not transactions:
        return []

    return transactions


def export_transactions(transactions):
    if not transactions:
        return "No Transactions"

    return "\n".join(transactions)
