import calendar

# Dictionary to store events with dates as keys
events = {}

def display_calendar(year, month):
    # Display the calendar for the given month and year
    print(calendar.month(year, month))

def add_event(year, month, day, event):
    # Add an event to the dictionary
    date = f"{year}-{month:02d}-{day:02d}"
    if date in events:
        events[date].append(event)
    else:
        events[date] = [event]
    print(f"Event added for {date}: {event}")

def view_events(year, month, day):
    # View events for a specific date
    date = f"{year}-{month:02d}-{day:02d}"
    if date in events:
        print(f"Events on {date}:")
        for event in events[date]:
            print(f"- {event}")
    else:
        print(f"No events found for {date}.")

def main():
    while True:
        print("\nSimple Calendar Application")
        print("1. Display Calendar")
        print("2. Add Event")
        print("3. View Events")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            year = int(input("Enter year (e.g., 2024): "))
            month = int(input("Enter month (1-12): "))
            display_calendar(year, month)
        
        elif choice == '2':
            year = int(input("Enter year (e.g., 2024): "))
            month = int(input("Enter month (1-12): "))
            day = int(input("Enter day (1-31): "))
            event = input("Enter event description: ")
            add_event(year, month, day, event)
        
        elif choice == '3':
            year = int(input("Enter year (e.g., 2024): "))
            month = int(input("Enter month (1-12): "))
            day = int(input("Enter day (1-31): "))
            view_events(year, month, day)
        
        elif choice == '4':
            print("Exiting the application.")
            break
        
        else:
            print("Invalid choice. Please choose an option from 1 to 4.")

if __name__ == "__main__":
    main()

