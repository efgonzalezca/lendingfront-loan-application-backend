def evaluate_loan(amount):
    """
    Evaluate a loan request based on the requested amount.

    Parameters:

    amount : float or int
        The requested loan amount. Must be a non-negative number.

    Return:
    str
        The loan decision one of "Approved", "Undecided", or "Declined".
    """
    if amount > 50000:
        decision = 'Declined'
    elif amount == 50000:
        decision = 'Undecided'
    else:
        decision = 'Approved'
    return decision
