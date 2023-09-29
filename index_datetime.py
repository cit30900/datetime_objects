#import datetime
from datetime import date, time, datetime, timezone

def main():
    # datetime module can create date, time, and datetime objects

    # Get a date object
    d = date.today() # Based on computer settings
    print(f"Date object: {d}")
    print(f"Date year: {d.year}")
    print(f"Date month: {d.month}")
    print(f"Date day: {d.day}")
    
    # Create a time object
    t = time(12, 10, 30)
    print(f"Time object: {t}")
    print(f"Time object timezone: {t.tzname()}")

    # Get a datetime object
    # dt = datetime.now() # <--- Creates a naive object
    dt = datetime.now(timezone.utc) # <---- Creates a timezone aware object
    print(f"DateTime object: {dt}")
    print(f"Datetime object timezone: {dt.tzname()}")
    print(f"DateTime year: {dt.year}")
    print(f"DateTime month: {dt.month}")
    print(f"DateTime day: {dt.day}")
    print(f"DateTime hour: {dt.hour}")
    print(f"DateTime minute: {dt.minute}")
    print(f"DateTime second: {dt.second}")
    print(f"DateTime time zone: {dt.tzinfo}")

if __name__ == "__main__":
    main()