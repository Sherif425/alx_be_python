# daily_remibder.py
while True:
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound_input = input("Is it time-bound? (yes/no): ").lower()

    time_bound = (time_bound_input == 'yes')
    reminder_message = ""


    match priority:
        case 'high':
            if time_bound:
                reminder_message = f"Reminder: {task} is a high priority task that requires immediate attention today!"
            else:
                reminder_message = f"Reminder: {task} is a high priority task. Aim to complete it today." 
        case 'medium':
            if time_bound:
                reminder_message = f"Reminder: '{task}' is a medium priority task that requires attention today."
            else:
                reminder_message = f"Reminder: '{task}' is a medium priority task. Try to complete it soon."
        case 'low':
            if time_bound:
                reminder_message = f"Reminder: '{task}' is a low priority task, but you marked it as time-bound. Consider completing it when you have free time, but be mindful of any deadlines!"
            else:
                reminder_message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
        case _: 
            reminder_message = "Invalid priority entered. Please choose high, medium, or low."
    print(reminder_message)

    break
