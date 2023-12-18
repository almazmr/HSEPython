from datetime import datetime, timedelta

def date_range(start_date, end_date):
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        if start > end:
            return []
        dates = []
        current_date = start
        while current_date <= end:
            dates.append(current_date.strftime("%Y-%m-%d"))
            current_date += timedelta(days=1)
        return dates
    except ValueError:
        return []

start_date = '2022-01-01'
end_date = '2022-01-03'
result = date_range(start_date, end_date)
print(result)