import csv

# Sample student data
student_data = [
    {"rollno": "101", "name": "Aradhya", "branch": "Computer Science", "m1": 85, "m2": 90, "m3": 78},
    {"rollno": "102", "name": "Cristiano", "branch": "Electrical Engineering", "m1": 75, "m2": 88, "m3": 92},
    {"rollno": "103", "name": "Akrithi", "branch": "Mechanical Engineering", "m1": 92, "m2": 82, "m3": 89},
    # Add more students as needed
]

# Create and write data to the CSV file
with open("mark.csv", "w", newline="") as file:
    fieldnames = ["rollno", "name", "branch", "m1", "m2", "m3"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # Write the header row
    writer.writeheader()
    
    # Write the student data
    writer.writerows(student_data)

print("CSV file 'mark.csv' has been created with sample student data.")
