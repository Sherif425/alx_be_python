from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(f"Current Date and Time: {current_date}")


def display_future_date(days_ahead):
    """Display the date a certain number of days from now."""
    if days_ahead < 0:
        raise ValueError("Days ahead must be a non-negative integer.")
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_ahead)
    print(f"Date {days_ahead} days from now: {future_date}")

def main():
    """Main function to explore datetime functionalities."""    
    print("Datetime Exploration")
    display_current_datetime()
    
    days_ahead = int(input("Enter the number of days to see the future date: "))
    display_future_date(days_ahead)


if __name__ == "__main__":
    main()
