# ECOR 1042 Lab 6 - Individual submission for text_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Roman Britto"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101277222"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-94"

#==========================================#
# Place your script for your text_UI after this line

from load_data import load_data
from load_data import add_average
from sort import *
from histogram import histogram
from curve_fit import curve_fit


def UI() -> None:
    """Return nothing, act as a text user interface with certain commands.

    Preconditions: None
    """
    cmd = ""
    data = ""
    while cmd.upper() != "E":
        print("The available commands are:\n\tL)oad Data\n\tS)ort Data\n\tC)urve Fit\n\tH)istogram\n\tE)xit")
        cmd = input("Please type your command: ")

        # ---L Command---------
        if cmd.upper() == "L":
            file = input("Please enter the name of the file: ")
            filter_l = input(
                "Please enter the attribute to use as a filter: ")

            attributes = ["All", "School", "Age", "Failures", "Health"]
            while filter_l not in attributes:
                filter_l = input(
                    "Invalid filter. Please enter another attribute: ")

            if filter_l == "All":
                value = 0

            if filter_l == "School":
                value = input("Please enter the value of the attribute: ")

            else:
                value = int(
                    input("Please enter the value of the attribute: "))

            print('Data loaded')
            data = add_average(load_data(file, (filter_l, value)))

        # ---S Command---------
        elif cmd.upper() == "S":
            if data == "":
                print("File not loaded. Please, load a file first.")
            else:
                filter_s = input(
                    "Please enter the attribute you want to use for sorting:\n'Age'\t'StudyTime'\t'Failures'\t'G_Avg'\n")

                attributes_s = ['Age', 'StudyTime', 'Failures', 'G_Avg']
                while filter_s not in attributes_s:
                    filter_s = input(
                        "Invalid attribute. Please enter another attribute: ")

                order = input("Ascending (A) or Descending (D) order: ")

                allowed_orders = ['A', 'D']
                while order not in allowed_orders:
                    order = input(
                        "Invalid Order. Please enter Ascending (A) or Descending (D) order: ")

                if filter_s == 'Age':
                    sorted_data = sort_students_age_bubble(data, order)
                if filter_s == 'StudyTime':
                    sorted_data = sort_students_time_selection(data, order)
                if filter_s == 'Failures':
                    sorted_data = sort_students_failures_bubble(data, order)
                if filter_s == 'G_Avg':
                    sorted_data = sort_students_g_avg_insertion(data, order)

                display = input(
                    "Data Sorted. Do you want to display the data? (Y/N): ")
                if display.upper() == "Y":
                    print(sorted_data)

        # ---C Command---------
        elif cmd.upper() == "C":
            if data == "":
                print("File not loaded. Please, load a file first.")
            else:
                filter_c = input(
                    "Please enter the attribute you want to use to find the best fit for G_Avg: ")
                degree_c = int(input(
                    "Please enter the order of the polynomial to be fitted: "))
                print(curve_fit(data, filter_c, degree_c))

        # ---H Command---------
        elif cmd.upper() == "H":
            if data == "":
                print("File not loaded. Please, load a file first.")
            else:
                filter_h = input(
                    "Please enter the attribute you want to use for plotting: ")
                histogram(data, filter_h)

        else:
            if cmd.upper() != 'E':
                if data == "":
                    print("No such command")
                else:
                    print("Invalid command.")


if __name__ == "__main__":  # I was told by my TA to include this.
    UI()

# student-mat.csv
