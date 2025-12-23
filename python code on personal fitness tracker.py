def log_fitness_data():
    try:
        activity = input("Enter activity type (e.g., Running, Cycling, Walking): ")
        duration = input("Enter duration in minutes: ")
        calories = input("Enter estimated calories burned: ")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} | Activity: {activity} | Duration: {duration} mins | Calories Burned: {calories}\n"
        with open("fitness_log.txt", "a") as file:
            file.write(log_entry)
        print("\nFitness data successfully logged.")
    except ValueError:
        print("\nInvalid input. Please ensure duration and calories are numbers.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
