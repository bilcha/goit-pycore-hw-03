from datetime import datetime

def get_days_from_today(date):
    try:
        added_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print(f"{date} is not valid date")
    else:
        current_date = datetime.today().date()
        days_since = current_date.toordinal() - added_date.toordinal()
        print(days_since)

test_data = "2025-10-10"
get_days_from_today(test_data)