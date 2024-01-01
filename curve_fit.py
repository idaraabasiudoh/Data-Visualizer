# ECOR 1042 Lab 6 - Individual submission for curve_fit function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Madhav Ajish"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101272814"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-94"

#==========================================#
import scipy as sc
import numpy as np
# Place your curve_fit function after this line


def curve_fit(info: list[dict], compare: str, degree: int) -> str:
    """
    Function takes a list of dictionaries and generates a curve fit comparing the
    G_Avg and a specified attribute of the list, to a specified degree. If the 
    inputted degree is higher than the order of the data, then the data will be 
    interpolated rather than regressed. 

    Preconditions: The attribute to be compared will always correspond to numerical values.
    The degree provided will be from 1 to 5. All dictionaries will contain the "G_Avg" key.

    >>>curve_fit([{"Health":11,"G_Avg":90},{"Health":13,"G_Avg":80},{"Health":12,"G_Avg":67}], "Health", 2)
    'y = 17.9999999999995x^2 + -436.9999999999891x + 2718.9999999999427'
    >>>curve_fit([{"Failures":4,"G_Avg":50},{"Failures":2,"G_Avg":70},{"Failures":4,"G_Avg":94}], "Failures", 3)
    'y = 0.9999999999999977x + 68.0'
    >>>curve_fit([{"Age":16,"G_Avg":50},{"Age":17,"G_Avg":70},{"Age":19,"G_Avg":94},{"Age":18,"G_Avg":89},{"Age":20,"G_Avg":72}], "Age", 4)
    'y = -1.652022854971655e-12x^4 + -2.1666666665463454x^3 + 109.99999999671712x^2 + -1839.833333293565x + 10201.999999819529'
    """
    x = []
    yRaw = {}

    # A dictionary of lists holds all the G_Avg points for each corresponding attribute

    for i in info:
        if i.get(compare) not in x:
            x.append(i.get(compare))
            yRaw[i.get(compare)] = []

        yRaw[i.get(compare)].append(i.get("G_Avg"))

    # A new list for the averaged G_Avg points is made and G_Avg values are averaged into it

    y = []
    temp = 0

    for key in yRaw:
        for i in yRaw[key]:
            temp += i

        y.append(temp / len(yRaw[key]))
        temp = 0

    z = "y = "

    if degree > len(x):     # Checks if the number of data points is less that the specified order
        degree = len(x) - 1

    coef = np.polyfit(x, y, degree)

    counter = len(coef)

    for n in coef:
        if counter > 2:
            counter -= 1
            z += str(n) + "x^" + str(counter) + " + "
        elif counter == 2:
            counter -= 1
            z += str(n) + "x + "
        else:
            z += str(n)

    return z


# Do NOT include a main script in your submission
