# -*- coding: utf-8 -*-
"""EXCERCISE 4 CE157 COURSEWORK AUTUMN 2023.ipynb


**Question 4**
"""

# Function to filter employees by salary range
# Function to filter employees by salary range
def filter_by_salary_range(employee_list, start_salary, end_salary):
    # Create a list of tuples with names, titles, and salaries, sorted by salary (largest first)
    filtered_employees = [(name, title, int(salary)) for name, title, salary in sorted(employee_list, key=lambda x: int(x[2]), reverse=True) if start_salary <= int(salary) <= end_salary]

    # Display results
    if not filtered_employees:
        print("No employees match the specified salary range.")
    else:
        print("\nFiltered employees (sorted by salary, largest first):")
        for name, title, salary in filtered_employees:
            print(f"{name}: {title} - Salary: {salary}")


# Function to filter employees by job title
def filter_by_job_title(employee_list, job_title_part):
    # Create a list of tuples with names and titles that contain the specified job title part
    filtered_employees = [(name, title) for name, title, *_ in employee_list if job_title_part.lower() in title.lower()]

    # Display results
    if not filtered_employees:
        print(f"No employees have a job title containing '{job_title_part}'.")
    else:
        print("\nFiltered employees (by job title):")
        for name, title in filtered_employees:
            print(f"{name}: {title}")

def main():
    try:
        # Input: File name containing employee data
        file_name = input("Enter the file name: ")

        # Read employee data from the file and create a list of tuples
        with open(file_name, 'r') as file:
            employee_data = [tuple(line.strip().split(',')) for line in file]
            print("\nList of tuples:")
            print(employee_data)

        # User interaction loop
        while True:
            print("\nSelect a function:")
            print("1. Filter by salary range")
            print("2. Filter by job title")
            print("3. Quit")

            # User choice
            choice = input("Enter your choice (1, 2, or 3): ")

            # Function execution based on user choice
            if choice == '1':
                start_salary = int(input("Enter the start salary: "))
                end_salary = int(input("Enter the end salary: "))
                filter_by_salary_range(employee_data, start_salary, end_salary)
            elif choice == '2':
                job_title_part = input("Enter part of the job title: ")
                filter_by_job_title(employee_data, job_title_part)
            elif choice == '3':
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found. Exiting the program.")

if __name__ == "__main__":
    main()
