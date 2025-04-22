import numpy as np

# Create a 1D array filled with random values
random_array = np.random.randint(1, 100, 16)  # Random values between 1 and 100

# Modify the array to a 4x4 NumPy array
modified_array = random_array.reshape(4, 4)

# Compute column-wise max value
column_max = np.max(modified_array, axis=0)

# Extract the second row as a 1D array
second_row = modified_array[1, :]

# Print results
print("Original 1D Array:\n", random_array)
print("\nModified 4x4 Array:\n", modified_array)
print("\nColumn-wise Max Values:\n", column_max)
print("\nExtracted Second Row:\n", second_row)



def count_above_average(scores):
    average = sum(scores) / len(scores)
    return len([score for score in scores if score > average])

# List of 10 student scores
student_scores = [85, 92, 78, 88, 95, 60, 72, 89, 91, 84]

# Find highest, lowest, and average score
highest = max(student_scores)
lowest = min(student_scores)
average = sum(student_scores) / len(student_scores)

# Count students above average
above_average_count = count_above_average(student_scores)

# Sort the list in ascending order
sorted_scores = sorted(student_scores)

# Check if all students scored above 50
all_passed = all(score > 50 for score in student_scores)

# Print results
print("Highest Score:", highest)
print("Lowest Score:", lowest)
print("Average Score:", average)
print("Number of Students Above Average:", above_average_count)
print("Sorted Scores:", sorted_scores)
print("Class Passed:", "Yes" if all_passed else "No")




import pandas as pd

# Create the employee data
data = {
    "Name": ["John", "Alice", "Bob", "Charlie"],
    "Age": [29, 34, 45, 38],
    "Salary": [50000, 75000, 120000, 95000],
    "Department": ["HR", "Finance", "Engineering", "Marketing"]
}

# Create a DataFrame
employee_df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
employee_df.to_csv("employee_data.csv", index=False)

# Load the CSV file into a DataFrame
employee_df = pd.read_csv("employee_data.csv")

# Print the DataFrame
print("Employee DataFrame:\n", employee_df)

# Filter employees with salary > 80,000
high_salary_employees = employee_df[employee_df["Salary"] > 80000]
print("\nEmployees with Salary > 80,000:\n", high_salary_employees)

# Add a new column "Experienced" based on age > 35
employee_df["Experienced"] = employee_df["Age"] > 35

# Remove the "Department" column
employee_df.drop("Department", axis=1, inplace=True)

# Print the updated DataFrame
print("\nUpdated DataFrame (without Department):\n", employee_df)

# Show summary and descriptive statistics
print("\nSummary of DataFrame:\n", employee_df.info())
print("\nDescriptive Statistics:\n", employee_df.describe())
