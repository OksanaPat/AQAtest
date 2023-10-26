from datetime import datetime

def calculate_age(birth_date):
    current_date = datetime.now()
    age = current_date - birth_date
    age_timestamp = age.total_seconds()
    return age, age_timestamp

# Example usage:
# Replace this with your birth date
provided_date = datetime(1993, 6, 2, 0, 0, 0)

# Calculate the age and the age in timestamp format
age, age_timestamp = calculate_age(provided_date)

# Print the result
print(f"Your exact age is {age}.")
print(f"Your exact age in timestamp format is {age_timestamp}.")