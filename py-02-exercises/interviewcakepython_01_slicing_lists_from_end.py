def show_balances(daily_balances):
    '''
    Prints pairs of adjacent balances for the last 3 days.

    >>> daily_balances = [107.92, 108.67, 109.86, 110.15]
    >>> show_balances(daily_balances)
    slice starting 3 days ago: [108.67, 109.86]
    slice starting 2 days ago: [109.86, 110.15]
    '''
    for day in range(-3, -1):
        daily_balance = [daily_balances[day], daily_balances[day+1]]
        print(f'slice starting {abs(day)} days ago: {daily_balance}')
