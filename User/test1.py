import enum

# Define an enum class for weekdays
class Weekday():
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

# Function to print the name and value of a weekday
def print_weekday(day):
    print(f"Day: {day.name}, Value: {day.value}")

# Main program
if __name__ == "__main__":
    # Using the enum
    today = Weekday.MONDAY

    print_weekday(today)
