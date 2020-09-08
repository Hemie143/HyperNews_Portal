from datetime import datetime


def get_release_date(release_str):
    data = release_str.split(':')[1]
    data = data.strip()
    return datetime.strptime(data, "%d %B %Y")
