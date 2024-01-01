# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Madhav Ajish, Jonathon Miller, Roman Britto, Idara-Abasi Udoh"

# Update "" with your team (e.g. T102)
__team__ = "T-94"

#==========================================#
# Place your sort_students_age_bubble function after this line
def sort_students_age_bubble(students: list[dict], order: str) -> list[dict]:
    """Function takes a list of dictionaries of student profiles, and sorts 
    the list based on increasing or decreasing order ('A' for ascending, 'D' for 
    descending) of age. If the key 'Age' is present in the dictionary, the list 
    is sorted as described above. If the key 'Age' is not present, an error 
    message is displayed, and the original list is returned. 
    
    Preconditions: Keys in all dictionaries in the the list 'students' must be 
    the same. 
    
    >>>sort_students_age_bubble([{"Age":10,"School":"GP"},{"Age":19,"School":"MS"}],
    "D")
   
    [{"Age": 19, "School":"MS"}, {"Age":10, "School":"GP"}]
    
    >>>sort_students_age_bubble([{"School":"GP"}, {"School":"MS"}], "D")
   
    "Age" key is not present.
    [{"School":"GP"}, {"School":"MS"}]
    
    >>>sort_students_age_bubble([{"School": "GP", "Age": 45}, {"School": "MS", 
    "Age": 33}], "A")
   
    [{"School": "MS", "Age": 33}, {"School": "GP", "Age": 45}]
    """
    if "Age" in students[0]:
        if order == "A":
            swap = True
            while swap:
                swap = False
                for i in range(len(students) - 1):
                    if students[i]["Age"] > students[i + 1]["Age"]:
                        students[i], students[i+1] = students[i + 1], students[i]
                        swap = True
        elif order == "D":
            swap = True
            while swap:
                swap = False
                for j in range(len(students) - 1):
                    if students[j]["Age"] < students[j + 1]["Age"]:
                        students[j], students[j+1] = students[j+1], students[j]
                        swap = True
        else:
            print("Invalid order input, please enter either 'A' or 'D'")

    else:
        print("Error, dictionary key 'Age' not found in dictionaries of list 'students'")

    return students
#==========================================#
# Place your sort_students_time_selection function after this line
def sort_students_time_selection(inputList: list[dict], order: str) -> list[dict]:
    """
    Returns the inputted list of dictionaries sorted with the selection sort 
    method in either ascending or descending order of time spent studying.
    
    Preconditions: All input parameters must be valid and that there are no 
    duplicate data entries.
    
    >>>sort_students_time_selection([{"StudyTime": 15.2,"School":"GP"},{"StudyTime": 18.1,"School":"MS"}], "D")
    [{"StudyTime": 18.1, "School":"MS"}, {"StudyTime":15.2, "School":"GP"}]
    >>>sort_students_time_selection([{"StudyTime": 14.1, "School":"MS"}, {"StudyTime":20.2, "School":"GP"}], "A")
    [{"StudyTime": 14.1, "School":"MS"}, {"StudyTime":20.2, "School":"GP"}]
    >>>sort_students_time_selection([{"School":"GP"},{"School":"MS"}], "D")
    "StudyTime" key is not present
    [{"School":"GP"}, {"School":"MS"}]
    """
    if "StudyTime" in inputList[0].keys():
        
        if order == "A":
            for i in range(len(inputList)):
                mindex = i
                for j in range(i + 1, len(inputList)):
                    if inputList[j].get("StudyTime") < inputList[i].get("StudyTime"):
                        mindex = j

                    inputList[i], inputList[mindex] = inputList[mindex], inputList[i]
                    
        if order == "D":
            for i in range(len(inputList)):
                mindex = i
                for j in range(i + 1, len(inputList)):
                    if inputList[j].get("StudyTime") > inputList[i].get("StudyTime"):
                        mindex = j
                        
                    inputList[i], inputList[mindex] = inputList[mindex], inputList[i]

        return inputList
        
    else:
        print('"StudyTime" key is not present')
        return inputList
#==========================================#
# Place your sort_students_g_avg_insertion function after this line
def sort_students_g_avg_insertion(stats: list, order: str) -> list:
    """Return the list of the students’ dictionaries sorted by the “G_Avg” attribute using insertion sort, in ascending or descending order depending on an indication of "A" or "D".

    Preconditions: stats must be a valid list of student dictionaries, order must be a valid string as either "A" or "D".

    >>> sort_students_g_avg_insertion([{'G_Avg': 7.2, 'School': 'GP'}, {'G_Avg': 6, 'School': 'GP'}, {'G_Avg': 100, 'School': 'MS'}], "D")
    [{'G_Avg': 100, 'School': 'MS'}, {'G_Avg': 7.2, 'School': 'GP'}, {'G_Avg': 6, 'School': GP'}]

    >>> sort_students_g_avg_insertion([{"G_Avg": 7.2, "School": "GP"}, {"G_Avg": 9.1, "School": "MS"}, {"G_Avg": 72, "School": "GP"}, {"G_Avg": 100, "School": "MS"}, {"G_Avg": 8, "School": "GP"}, {"G_Avg": 10, "School": "MS"}], "A")
    [{'G_Avg': 7.2, 'School': 'GP'}, {'G_Avg': 8, 'School': 'GP'}, {'G_Avg': 9.1, 'School': 'MS'}, {'G_Avg': 10, 'School': 'MS'}, {'G_Avg': 72, 'School': 'GP'}, {'G_Avg': 100, 'School': 'MS'}]
    """

    if "G_Avg" in stats[0]:  # assuming dictionaries have the same keys
        if order == "A":
            for i in range(1, len(stats)):
                dic = stats[i]
                j = i - 1
                while j >= 0 and dic["G_Avg"] < stats[j]["G_Avg"]:
                    stats[j + 1] = stats[j]
                    j -= 1
                stats[j + 1] = dic
        elif order == "D":
            for i in range(1, len(stats)):
                dic = stats[i]
                j = i - 1
                while j >= 0 and dic["G_Avg"] > stats[j]["G_Avg"]:
                    stats[j + 1] = stats[j]
                    j -= 1
                stats[j + 1] = dic
        return stats
    else:
        print("“G_Avg” key is not present")
        return stats

#==========================================#
# Place your sort_students_failures_bubble function after this line
def sort_students_failures_bubble(failure_list: list[dict], order: str) -> list[dict]:
    """ Sorts a list of dictionaries containing student information by the "Failures" attribute in either ascending or descending order using bubble sort algorithm.

    >>>sort_students_failures_bubble([{"Failures":12,"School":"GP"},{"Failures":20,"School":"MS"},{"Failures":15, "School":"GP"}], "D")
    [{'Failures': 20, 'School': 'MS'}, {'Failures': 15, 'School': 'GP'}, {'Failures': 12, 'School': 'GP'}]

    >>>sort_students_failures_bubble([{"Failures":12,"School":"GP"},{"Failures":20,"School":"MS"},{"Failures":15, "School":"GP"}], "A")
    [{'Failures': 12, 'School': 'GP'}, {'Failures': 15, 'School': 'GP'}, {'Failures': 20, 'School': 'MS'}]

    >>>sort_students_failures_bubble([{"School":"MS"}, {"School":"GP"}], "A")
    One or more dictionaries does not have the "Failure" key
    [{'School': 'MS'}, {'School': 'GP'}]
    """
    for dic in failure_list:
        if 'Failures' not in dic in failure_list:
            print('One or more dictionaries does not have the "Failure" key')
            return failure_list

    n = len(failure_list)

    for i in range(n):
        for j in range(0, n - i - 1):
            if order == "A":
                if failure_list[j]["Failures"] > failure_list[j + 1]["Failures"]:
                    failure_list[j], failure_list[j +
                                                  1] = failure_list[j + 1], failure_list[j]
            elif order == "D":
                if failure_list[j]["Failures"] < failure_list[j + 1]["Failures"]:
                    failure_list[j], failure_list[j +
                                                  1] = failure_list[j + 1], failure_list[j]

    return failure_list
#==========================================#
# Place your sort function after this line
def sort_by_key(inputList: list[dict], order: str, key: str) -> list[dict]:
    """
    Sorts a list of dictionaries in either ascending or descending values, by
    the key given as a parameter.
    
    Preconditions: All input parameters must be valid and that there are no 
    duplicate data entries.
    
    >>>sort_by_key([{"Failures":12,"School":"GP"},{"Failures":20,"School":"MS"},{"Failures":15, "School":"GP"}], "A", "Failures")
    [{'Failures': 12, 'School': 'GP'}, {'Failures': 15, 'School': 'GP'}, {'Failures': 20, 'School': 'MS'}]
    >>>sort_by_key([{"Age":10,"School":"GP"},{"Age":19,"School":"MS"}],"D","Age")
    [{'Age': 19, 'School': 'MS'}, {'Age': 10, 'School': 'GP'}]
    >>>sort_by_key([{"School":"GP"},{"School":"MS"}], "D", "School")
    Cannot be sorted by "School"
    [{'School': 'GP'}, {'School': 'MS'}]
    """
    if key == "Age":
        return sort_students_age_bubble(inputList, order)
    elif key == "StudyTime":
        return sort_students_time_selection(inputList, order)
    elif key == "G_Avg":
        return sort_students_g_avg_insertion(inputList, order)
    elif key == "Failures":
        return sort_students_failures_bubble(inputList, order)
    else:
        print('Cannot be sorted by "' + key + '"')
        return inputList
# Do NOT include a main script in your submission
