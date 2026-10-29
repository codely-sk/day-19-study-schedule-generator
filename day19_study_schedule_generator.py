
from datetime import datetime, timedelta


def get_positive_number(message):
    while True:
        try:
            number = float(input(message))

            if number > 0:
                return number

            print("Please enter a number greater than zero.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def get_subjects():
    subjects = []

    count = int(get_positive_number("How many subjects? "))

    for i in range(int(count)):
        print(f"\nSubject {i + 1}")

        name = input("Enter subject name: ").strip()

        while not name:
            print("Subject name cannot be empty.")
            name = input("Enter subject name: ").strip()

        print("Priority: 1 = High, 2 = Medium, 3 = Low")

        while True:
            priority = input("Enter priority (1/2/3): ").strip()

            if priority in ["1", "2", "3"]:
                break

            print("Please enter 1, 2, or 3.")

        duration = get_positive_number(
            "Desired study duration in minutes: "
        )

        subjects.append({
            "name": name,
            "priority": int(priority),
            "duration": duration
        })

    return subjects


def generate_schedule(subjects, available_minutes, start_time):
    # Sort high-priority subjects first.
    subjects.sort(key=lambda subject: subject["priority"])

    current_time = start_time
    remaining_minutes = available_minutes
    schedule = []

    for subject in subjects:
        if remaining_minutes <= 0:
            break

        # Fit the subject into the time still available.
        study_minutes = min(
            subject["duration"],
            remaining_minutes
        )

        end_time = current_time + timedelta(minutes=study_minutes)

        schedule.append({
            "name": subject["name"],
            "priority": subject["priority"],
            "start": current_time.strftime("%I:%M %p"),
            "end": end_time.strftime("%I:%M %p"),
            "duration": study_minutes
        })

        current_time = end_time
        remaining_minutes -= study_minutes

    return schedule, remaining_minutes


def display_schedule(schedule, remaining_minutes):
    print("\n========== YOUR STUDY TIMETABLE ==========")

    if not schedule:
        print("No study sessions could be scheduled.")
        return

    print(f"{'Subject':<20} {'Start':<10} {'End':<10} {'Minutes':>8}")
    print("-" * 52)

    total_study_minutes = 0

    for session in schedule:
        print(
            f"{session['name'][:20]:<20} "
            f"{session['start']:<10} "
            f"{session['end']:<10} "
            f"{session['duration']:>8.1f}"
        )

        total_study_minutes += session["duration"]

    print("-" * 52)
    print(f"Total scheduled study time: {total_study_minutes:.1f} minutes")
    print(f"Unused available time: {remaining_minutes:.1f} minutes")

    print("\nPriority key: 1 = High, 2 = Medium, 3 = Low")


def main():
    print("===== STUDY SCHEDULE GENERATOR =====")

    subjects = get_subjects()

    available_hours = get_positive_number(
        "\nHow many hours can you study today? "
    )
    available_minutes = available_hours * 60

    while True:
        start_input = input(
            "Enter your starting time (HH:MM, 24-hour format): "
        ).strip()

        try:
            start_time = datetime.strptime(start_input, "%H:%M")
            break
        except ValueError:
            print("Invalid time. Example: 09:30 or 14:00.")

    schedule, remaining = generate_schedule(
        subjects,
        available_minutes,
        start_time
    )

    display_schedule(schedule, remaining)


if __name__ == "__main__":
    main()
