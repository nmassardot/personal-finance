import datetime

def get_last_month_total_response(account):
    total = 0

    now = datetime.datetime.now()
    month_ago = now - datetime.timedelta(days=30)
    iso_month_ago = month_ago.isoformat()

    movements = account.movements.all(since=iso_month_ago)

    for movement in movements:
        total += int(movement.amount)


    respose = {
        "info": "from 30 days ago to today",
        "total": total
    }

    return respose
