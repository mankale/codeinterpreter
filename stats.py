#!pip install bedrock-agentcore pandas

# Calculate average salary from employee_salaries.csv
import pandas as pd

# Read the CSV file
df = pd.read_csv('data.csv')

# Display the first few rows of the dataframe
print("First 5 rows of the dataset:")
print(df.head())

# Calculate the average salary
average_salary = df['salary_usd'].mean()

# Display the result
print(f"\nAverage Salary: ${average_salary:.2f}")

# Additional statistics
print(f"\nSalary Statistics:")
print(f"Minimum Salary: ${df['salary_usd'].min():.2f}")
print(f"Maximum Salary: ${df['salary_usd'].max():.2f}")
print(f"Median Salary: ${df['salary_usd'].median():.2f}")
print(f"Standard Deviation: ${df['salary_usd'].std():.2f}")
