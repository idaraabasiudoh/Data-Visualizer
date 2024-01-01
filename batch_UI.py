# ECOR 1042 Lab 6 - Individual submission for batch_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Idara-Abasi Udoh"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101244376"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-94"

#==========================================#
# Place your script for your batch_UI after this line
from load_data import *
from sort import *
from curve_fit import *
from histogram import *

filename = input(
    'Please enter the name of the file where your commands are stored \n')

with open(filename, 'r') as f:
    command = f.readline()

command = command.strip('\n').split(';')

# ---L Command---------
if command[0].upper() == "L":
    file = command[1]
    filter_l = command[2]

    attributes = ["All", "School", "Age", "Failures", "Health"]
    if filter_l not in attributes:
        print("Invalid filter. Please use another attribute")

    if filter_l == "All":
        value = 0

    if filter_l == 'School':
        value = command[3]

    else:
        value = int(command[3])

    print('Data loaded')
    data = add_average(load_data(file, (filter_l, value)))


with open(filename, 'r') as f:
    lines = f.readlines()[1:]
    lines = [one.strip('\n').split(';') for one in lines]

    for line in lines:
        # ---S Command---------
        if line[0].upper() == "S":
            if data == "":
                print("File not loaded. Please, load a file first.")
            else:
                filter_s = line[1]

                attributes_s = ['Age', 'StudyTime', 'Failures', 'G_Avg']
                if filter_s not in attributes_s:
                    filter_s = print(
                        "Invalid attribute. Please use another attribute")

                order = line[2]

                allowed_orders = ['A', 'D']
                if order not in allowed_orders:
                    order = print(
                        "Invalid Order. Please use Ascending (A) or Descending (D) order")

                if filter_s == 'Age':
                    sorted_data = sort_students_age_bubble(data, order)
                if filter_s == 'StudyTime':
                    sorted_data = sort_students_time_selection(data, order)
                if filter_s == 'Failures':
                    sorted_data = sort_students_failures_bubble(data, order)
                if filter_s == 'G_Avg':
                    sorted_data = sort_students_g_avg_insertion(data, order)

                display = line[3]
                if display.upper() == "Y":
                    print(sorted_data)

        # ---C Command---------
        elif line[0].upper() == "C":
            if data == "":
                print("File not loaded. Please, load a file first.")
            else:
                filter_c = line[1]
                degree_c = int(line[2])
                print(curve_fit(data, filter_c, degree_c))

        # ---H Command---------
        elif line[0].upper() == "H":
            if data == "":
                print("File not loaded. Please, load a file first.")
            else:
                filter_h = line[1]
                histogram(data, filter_h)

        else:
            if line[0].upper() != 'E':
                if data == "":
                    print("No such command")
                else:
                    print("Invalid command.")



