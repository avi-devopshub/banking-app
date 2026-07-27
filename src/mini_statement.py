def get_mini_statement(transactions):
    if not transactions:
        return []

    return transactions[-5:]
