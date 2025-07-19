task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

reminder = f"'{task}' is a {priority} priority task"

match priority:
    case "high":
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Please address it soon."
    case "medium":
        if time_bound == "yes":
            reminder += " that should be completed today."
        else:
            reminder += ". Plan to complete it soon."
    case "low":
        if time_bound == "yes":
            reminder += " but needs to be done today."
        else:
            reminder += ". Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority entered. Please use high, medium, or low."

print(f"Reminder: {reminder}")
