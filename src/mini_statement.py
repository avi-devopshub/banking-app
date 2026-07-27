def get_mini_statement(transactions):
    if not transactions:
        return []

    return transactions[-5:]


def export_transactions(transactions):
    if not transactions:
        return "No Transactions"

    return "\n".join(transactions)
