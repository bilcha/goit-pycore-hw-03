from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    current_day = datetime.today().date()

    days_until_next_sunday = (6 - current_day.weekday()) % 7
    one_week_later = current_day + timedelta(days=days_until_next_sunday + 7) 

    birthdays_next_week = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        birthday_this_year = birthday.replace(year=current_day.year)

        if birthday_this_year < current_day:
            birthday_this_year = birthday_this_year.replace(year=current_day.year + 1)

        adjusted_birthday = birthday_this_year
        if birthday_this_year.weekday() in [5, 6]:
            adjusted_birthday = birthday_this_year + timedelta(days=(7 - birthday_this_year.weekday()))

        if current_day <= birthday_this_year <= one_week_later or current_day <= adjusted_birthday <= one_week_later:
            birthdays_next_week.append({"name": user["name"], "birthday": adjusted_birthday})
    
    return birthdays_next_week

users = [
    {"name": "John Doe", "birthday": "1985.12.05"},
    {"name": "Jane Smith", "birthday": "1990.12.27"},
    {"name": "Joe Tribiany", "birthday": "1990.12.08"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print(upcoming_birthdays)
