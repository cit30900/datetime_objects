from datetime import datetime, timezone
import pytz

def main():
    # strFtime (string FROM time) - takes a datetime object and converts it into a string according to the format codes
    # INSTANCE method (works on a datetime object)
    
    dt = datetime.now(timezone.utc)
    format_string = '%m/%d/%y'
    print(dt.strftime(format_string))

    format_string = '%A %B %d, %Y'
    print(dt.strftime(format_string))

    format_string = '%H:%M %z'
    print(dt.strftime(format_string))

    format_string = '%A %B %d, %Y %I:%M%p %Z'
    print(dt.strftime(format_string))

    # strPtime (string PARSE time) - takes a well-formatted string and converts it into a datetime object
    # CLASS method (runs on the datetime class itself, not an instance of datetime)
    # Produces a naive object
    time_string = "2022-07-01 00:18:38 EST"
    format_string = "%Y-%m-%d %H:%M:%S %Z"
    dt = datetime.strptime(time_string, format_string)
    print(f"Datetime object: {dt}")
    print(f'DateTime time zone: {dt.tzinfo}') # Naive object

    # Need to assign a timezone to our datetime object
    # Use pytz to create an object of class timezone
    est_timezone = pytz.timezone("US/Eastern")

    # Make a timezone-aware datetime object
    parsed_dt = est_timezone.localize(dt)

    print(f'Datetime object: {parsed_dt}')
    print(f'DateTime time zone: {parsed_dt.tzinfo}') # Aware object

if __name__ == "__main__":
    main()