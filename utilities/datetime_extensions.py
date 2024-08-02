from datetime import datetime

def convert_to_datetime(date_string):
    date = datetime.strptime(date_string, '%Y-%m-%d')
    return date

def convert_to_date_string(date):
    day = date.day
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]

    date_string = date.strftime(f'%B %e{suffix}, %Y')
    return date_string

def calculate_time_since_string(date_string):
    years_since_release = (datetime.now() - datetime.strptime(date_string, '%Y-%m-%d')).total_seconds() / (365.2425 * 24 * 60 * 60)

    if years_since_release < 1 / 12:
        release_duration_string = f"{round(years_since_release * 365.2425) - 1} day{'s' if round(years_since_release * 365.2425) - 1 > 1 else ''} ago"
    elif years_since_release < 1:
        release_duration_string = f"{round(years_since_release * 12)} month{'s' if round(years_since_release * 12) > 1 else ''} ago"
    else:
        release_duration_string = f"{round(years_since_release)} year{'s' if round(years_since_release) > 1 else ''} ago"

    return release_duration_string