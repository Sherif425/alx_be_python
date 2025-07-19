while True:
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound_input = input("Is it time-bound? (yes/no): ").lower()

    is_time_bound = (time_bound_input == 'yes')

    base_reminder = ""
    time_sensitivity_phrase = "" 
    
    match priority:
        case 'high':
            base_reminder = f"'{task}' is a high priority task"
            if is_time_bound:
                time_sensitivity_phrase = " that requires immediate attention today!"
            else:
                time_sensitivity_phrase = ". Aim to complete it today."
        case 'medium':
            base_reminder = f"'{task}' is a medium priority task"
            if is_time_bound:
                time_sensitivity_phrase = " that requires attention today."
            else:
                time_sensitivity_phrase = ". Try to complete it soon."
        case 'low':
            base_reminder = f"'{task}' is a low priority task"
            if is_time_bound:
                time_sensitivity_phrase = ". While low priority, you marked it as time-bound, so consider acting soon!"
            else:
                time_sensitivity_phrase = ". Consider completing it when you have free time."
        case _:
            print("Invalid priority entered. Please choose high, medium, or low.")
            break 
            
    if base_reminder:
        final_reminder = ""
        if priority == 'low' and not is_time_bound:
            final_reminder = f"Note: {base_reminder}{time_sensitivity_phrase}"
        else:
            final_reminder = f"Reminder: {base_reminder}{time_sensitivity_phrase}"
        
        print(final_reminder)
    
    break
