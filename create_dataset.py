import csv

# Fictional student dataset for CUL-CYB 371: Data Mining and Data Warehousing
students = [
    {"Student ID": "CS2026001", "Department": "Computer Science", "Level": 200, "Attendance Percentage": 92, "Average Examination Score": 78},
    {"Student ID": "CS2026002", "Department": "Computer Science", "Level": 200, "Attendance Percentage": 85, "Average Examination Score": 69},
    {"Student ID": "CY2026003", "Department": "Cyber Security", "Level": 300, "Attendance Percentage": 96, "Average Examination Score": 88},
    {"Student ID": "IS2026004", "Department": "Information Systems", "Level": 200, "Attendance Percentage": 81, "Average Examination Score": 65},
    {"Student ID": "CS2026005", "Department": "Computer Science", "Level": 300, "Attendance Percentage": 89, "Average Examination Score": 74},
    {"Student ID": "SE2026006", "Department": "Software Engineering", "Level": 400, "Attendance Percentage": 94, "Average Examination Score": 91},
    {"Student ID": "CY2026007", "Department": "Cyber Security", "Level": 200, "Attendance Percentage": 76, "Average Examination Score": 58},
    {"Student ID": "CS2026008", "Department": "Computer Science", "Level": 400, "Attendance Percentage": 98, "Average Examination Score": 84},
    {"Student ID": "IS2026009", "Department": "Information Systems", "Level": 300, "Attendance Percentage": 87, "Average Examination Score": 72},
    {"Student ID": "SE2026010", "Department": "Software Engineering", "Level": 200, "Attendance Percentage": 90, "Average Examination Score": 80},
    {"Student ID": "CS2026011", "Department": "Computer Science", "Level": 200, "Attendance Percentage": 72, "Average Examination Score": 61},
    {"Student ID": "CY2026012", "Department": "Cyber Security", "Level": 400, "Attendance Percentage": 93, "Average Examination Score": 86},
    {"Student ID": "IS2026013", "Department": "Information Systems", "Level": 400, "Attendance Percentage": 84, "Average Examination Score": 77},
    {"Student ID": "SE2026014", "Department": "Software Engineering", "Level": 300, "Attendance Percentage": 88, "Average Examination Score": 73},
    {"Student ID": "CS2026015", "Department": "Computer Science", "Level": 300, "Attendance Percentage": 79, "Average Examination Score": 67},
]

# Save the records as a CSV file that can be opened in Excel or imported into a database.
with open("student_dataset.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=students[0].keys())
    writer.writeheader()
    writer.writerows(students)

print(f"Created student_dataset.csv with {len(students)} fictional student records.")
