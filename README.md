# Day 19 — Study Schedule Generator 📚

A Python project that generates a personalized study timetable based on subject priorities, desired study durations, and available study time.

## ✨ Features

- Add multiple subjects to your timetable.
- Assign high, medium, or low priority to each subject.
- Enter the desired study duration for each subject.
- Automatically sort subjects by priority.
- Set your available study hours and starting time.
- Calculate start and end times for each study session.
- Fit the timetable within the available time.
- Display total scheduled study time and unused time.
- Validate numeric input and starting time.

## 🛠️ Technologies Used

- Python 3
- `datetime` module
- Lists and dictionaries
- Functions and loops
- Sorting with `lambda`
- Conditional statements
- Exception handling

## 📦 Installation

No external libraries are required. Install Python 3 if it is not already installed.

## ▶️ How to Run

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

```bash
python study_schedule_generator.py
```

5. Enter your subjects, priorities, and desired durations.
6. Enter your available study hours and starting time.
7. View your generated timetable in the terminal.

## 📊 Example

Suppose you have two hours available and enter these subjects:

| Subject | Priority | Desired Duration |
|---|---|---:|
| Python | High | 60 minutes |
| DSA | Medium | 45 minutes |
| TOC | Low | 30 minutes |

The program schedules high-priority subjects first and fits the sessions into your available time.

The final session may be shortened if the remaining time is less than its requested duration.

## 📚 Learning Objectives

This project demonstrates how to collect user input, organize data using lists and dictionaries, sort records by priority, perform time calculations, validate input, and generate a timetable using Python.

## 🚀 Future Improvements

- Add automatic breaks between study sessions.
- Save the timetable to a text or CSV file.
- Allow users to edit or remove subjects.
- Add a graphical user interface.
- Support different timetables for different days.

---

**Project 19 of 20** — Building practical Python skills one project at a time!