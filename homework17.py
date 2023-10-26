from datetime import datetime, timedelta

def add_days(input_date, days):
    return input_date + timedelta(days=days)
# Example usage:
given_date = datetime(2023, 9, 15, 12, 30, 0)  # Example datetime
days_to_add = 5  # Example number of days to add
result_date = add_days(given_date, days_to_add)
print("Result Date:", result_date)

def  subtract_days(input_date, days):
    return input_date - timedelta(days=days)
# Example usage:
given_date = datetime(2023, 9, 15, 12, 30, 0)  # Example datetime
days_to_subtract = 5  # Example number of days to subtract
result_date = subtract_days(given_date, days_to_subtract)
print("Result Date:", result_date)
