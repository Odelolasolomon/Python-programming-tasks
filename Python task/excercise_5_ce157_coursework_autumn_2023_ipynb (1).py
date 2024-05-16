# -*- coding: utf-8 -*-
"""EXCERCISE 5 CE157 COURSEWORK AUTUMN 2023.ipynb.ipynb

**Excercise 5**

****Cell 1: Import Libraries and Define Data Type****
"""

import numpy as np

# Define the named data type for the second array
student_dtype = np.dtype([('registration_number', int), ('exam_mark', int), ('coursework_mark', int), ('total_mark', int), ('grade', 'U10')])

"""**Cell 2: Define Grade Calculation Function**"""

def calculate_grade(rounded_exam, rounded_coursework, overall_mark):
    if rounded_exam < 35 or rounded_coursework < 35:
        return 'Fail'
    elif overall_mark >= 70:
        return 'Distinction'
    elif 60 <= overall_mark <= 69:
        return 'Merit'
    elif 45 <= overall_mark <= 59:
        return 'Pass'
    else:
        return 'Fail'

"""**Cell 3: Define File Processing Function**"""

# Function to process the input file
def process_file(file_name):
    try:
        with open(file_name, 'r') as file:
            # Read the first line to get the number of students and coursework weight
            num_students, num_coursework, coursework_weight = map(int, file.readline().split())

            # Create a 2-dimensional NumPy array with initial values
            array1 = np.zeros(num_students, dtype=student_dtype)

            # Read the remaining lines and populate array1
            for i in range(num_students):
                line = file.readline().split()
                registration_number, exam_mark, *coursework_marks = map(float, line)
                coursework_avg = sum(coursework_marks) / num_coursework
                overall_mark = (exam_mark * (1 - coursework_weight / 100)) + (coursework_avg * (coursework_weight / 100))

                # Populate the array1 with registration number, exam mark, coursework average, and overall mark
                array1[i] = (registration_number, exam_mark, coursework_avg, overall_mark, 0)

            # Create the second array with the named data type
            array2 = np.zeros(num_students, dtype=student_dtype)

            # Populate the second array with rounded values and grades
            for i in range(num_students):
                # Access individual elements of the NumPy array for rounding
                rounded_exam = round(array1[i]['exam_mark'])
                rounded_coursework = round(array1[i]['coursework_mark'])
                rounded_total_mark = round(array1[i]['total_mark'])

                grade = calculate_grade(rounded_exam, rounded_coursework, rounded_total_mark)

                # Populate the array2 with rounded values and grades
                array2[i] = (array1[i]['registration_number'], rounded_exam, rounded_coursework, rounded_total_mark, grade)

            # Sort array2 by overall mark
            sorted_array2 = np.sort(array2, order='total_mark')[::-1]

            # Output the sorted array to a file
            with open('ex5outputdata.txt', 'w') as output_file:
                np.savetxt(output_file, sorted_array2, fmt='%d, %.1f, %.1f, %.1f, %s', header='Reg. No, Exam, Coursework, Total, Grade', comments='')

            # Output statistics to the console
            num_distinction = np.count_nonzero(array2['grade'] == 'Distinction')
            num_merit = np.count_nonzero(array2['grade'] == 'Merit')
            num_pass = np.count_nonzero(array2['grade'] == 'Pass')
            num_fail = np.count_nonzero(array2['grade'] == 'Fail')
        

            print(f"\nNumber of Distinction grades: {num_distinction}")
            print(f"Number of Merit grades: {num_merit}")
            print(f"Number of Pass grades: {num_pass}")
            print(f"Number of Fail grades: {num_fail}")

            if num_fail > 0:
                failed_students = array2[array2['grade'] == 'Fail']['registration_number']
                print(f"\nRegistration numbers of students who have failed: {failed_students}")

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

# Example usage:
process_file(r'C:\Users\hp\Downloads\Excercises CE157\ex5data.txt')