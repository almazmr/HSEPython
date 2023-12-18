from datetime import datetime

moscow_times_date = "Wednesday, October 2, 2002"
guardian_date = "Friday, 11.10.13"
daily_news_date = "Thursday, 18 August 1977"

moscow_times_datetime = datetime.strptime(moscow_times_date, "%A, %B %d, %Y")
guardian_datetime = datetime.strptime(guardian_date, "%A, %d.%m.%y")
daily_news_datetime = datetime.strptime(daily_news_date, "%A, %d %B %Y")

print(moscow_times_datetime)
print(guardian_datetime)
print(daily_news_datetime)