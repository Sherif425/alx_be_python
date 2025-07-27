from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays and returns the current date and time formatted as 'YYYY-MM-DD HH:MM:SS'.
    """
    current_date = datetime.now()
    # Format the current date and time
    formatted_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_current_date}")
    return formatted_current_date # Return the formatted string

def calculate_future_date(days_ahead):
    """
    Calculates and prints the date a certain number of days from now,
    formatted as 'YYYY-MM-DD'.
    """
    if days_ahead < 0:
        raise ValueError("Days ahead must be a non-negative integer.")
    
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_ahead)
    
    # Format the future date as "YYYY-MM-DD"
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Date {days_ahead} days from now: {formatted_future_date}")
    return formatted_future_date # Return the formatted string (optional, but good practice)

def main():
    """Main function to explore datetime functionalities."""     
    print("Datetime Exploration")
    
    # Call display_current_datetime and use its return value if needed
    display_current_datetime()
    
    try:
        days_ahead = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days_ahead)
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid integer for days.")


if __name__ == "__main__":
    main()
