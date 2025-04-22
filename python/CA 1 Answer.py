print("#Question 1 :")
import numpy as np


random_array = np.random.randint(1, 100, 16)
print(random_array)

modified_array = random_array.reshape(4, 4)
print(modified_array)

column_max = np.max(modified_array, axis=0)
print(column_max)

second_row = modified_array[1, :]
print(second_row)

print("Original 1D Array:\n", random_array)
print("\nModified 4x4 Array:\n", modified_array)
print("\nColumn-wise Max Values:\n", column_max)
print("\nExtracted Second Row:\n", second_row)

print()

print("Question 2")

student_scores = [85, 92, 78, 88, 95, 60, 72, 89, 91, 84]
print(student_scores)

highest = max(student_scores)
lowest = min(student_scores)
average = sum(student_scores) / len(student_scores)
print("Highest Score:", highest)
print("Lowest Score:", lowest)
print("Average Score:", average)


def count_above_average(scores):
    average = sum(scores) / len(scores)
    return len([score for score in scores if score > average])

above_average_count = count_above_average(student_scores)
print("Number of Students Above Average:", above_average_count)


sorted_scores = sorted(student_scores)
print("Sorted Scores:", sorted_scores)


all_passed = all(score > 50 for score in student_scores)
print("Class Passed:", "Yes" if all_passed else "No")







print("Question 3")
import pandas as pd


data = {
    "Name": ["John", "Alice", "Bob", "Charlie"],
    "Age": [29, 34, 45, 38],
    "Salary": [50000, 75000, 120000, 95000],
    "Department": ["HR", "Finance", "Engineering", "Marketing"]
}


employee_df = pd.DataFrame(data)
employee_df.to_csv("employee_data.csv", index=False)

employee_df = pd.read_csv("employee_data.csv")
print("Employee DataFrame:\n", employee_df)


high_salary_employees = employee_df[employee_df["Salary"] > 80000]
print("\nEmployees with Salary > 80,000:\n", high_salary_employees)
print()

employee_df["Experienced"] = employee_df["Age"] > 35


employee_df.drop("Department", axis=1, inplace=True)


print("\nUpdated DataFrame (without Department):\n", employee_df)


print("\nSummary of DataFrame:\n", employee_df.info())
print("\nDescriptive Statistics:\n", employee_df.describe())





