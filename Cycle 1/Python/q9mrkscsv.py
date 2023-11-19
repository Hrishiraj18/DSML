import csv

# Initialize variables to store total marks and subject-wise sums and counts
total_marks = 0
subject_sums = {"m1": 0, "m2": 0, "m3": 0}
subject_counts = {"m1": 0, "m2": 0, "m3": 0}

# Initialize variables to keep track of the student with the highest and second highest marks
highest_mark_student = {"name": None, "marks": 0}
second_highest_mark_student = {"name": None, "marks": 0}

# Read data from the CSV file
with open("mark.csv", "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        rollno = row["rollno"]
        name = row["name"]
        m1 = float(row["m1"])
        m2 = float(row["m2"])
        m3 = float(row["m3"])
        
        # Calculate total marks
        total_marks += m1 + m2 + m3
        
        # Update subject-wise sums and counts
        subject_sums["m1"] += m1
        subject_sums["m2"] += m2
        subject_sums["m3"] += m3
        subject_counts["m1"] += 1
        subject_counts["m2"] += 1
        subject_counts["m3"] += 1
        
        # Check if the current student has the highest or second highest marks
        current_total_marks = m1 + m2 + m3
        if current_total_marks > highest_mark_student["marks"]:
            second_highest_mark_student = highest_mark_student.copy()
            highest_mark_student = {"name": name, "marks": current_total_marks}
        elif current_total_marks > second_highest_mark_student["marks"]:
            second_highest_mark_student = {"name": name, "marks": current_total_marks}

# Calculate the average marks for each subject
average_marks = {subject: subject_sums[subject] / subject_counts[subject] for subject in subject_sums}

# Print the results
print(f"Total Marks of All Students: {total_marks}")
print("Average Marks:")
for subject, average in average_marks.items():
    print(f"{subject}: {average}")
print(f"Student with the Highest Marks: {highest_mark_student['name']} ({highest_mark_student['marks']} marks)")
print(f"Student with the Second Highest Marks: {second_highest_mark_student['name']} ({second_highest_mark_student['marks']} marks)")
