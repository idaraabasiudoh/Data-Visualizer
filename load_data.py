# ECOR 1042 Lab 3 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Madhav Ajish, Roman Britto, Idara-Abasi Udoh, Jonathon Miller"

# Update "" with your team (e.g. T102)
__team__ = "T-94"

#==========================================#
# Place your student_school_list function after this line
def student_school_list(filename: str, schoolname: str) -> list[dict]:
    """
    Takes the name of the file where the data is stored and a school name as input.
    Returns a list of students (stored as a dictionary) that attended the school
    provided. The keys of the dictionary are the labels for all attributes in the
    spreadsheet except “School”.
    
    Preconditions: File must be the correct type and name, School must be a string.
    
    >>>student_school_list("student-mat.csv","XD")
    []
    >>>student_school_list("student-mat.csv","GP")
    [{'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 6,
    'G1': 5, 'G2': 6, 'G3': 6},
    {another element},
    ...
    """
    temp_dict = {}

    school_list = []

    data = open(filename, 'r')
    for line in data:
        if line.split(',')[0] == str(schoolname):
            lines = line.strip('\n').split(',')
            temp_dict = {'Age': int(lines[1]), 'StudyTime': float(lines[2]), 'Failures': int(lines[3]), 'Health': int(lines[4]),
                   'Absences': int(lines[5]), 'G1': int(lines[6]), 'G2': int(lines[7]), 'G3': int(lines[8])}
            school_list.append(temp_dict)

    data.close()

    return school_list

#==========================================#
# Place your student_health_list function after this line
def student_health_list(file: str, health: int) -> list[dict]:
    """Return a list of dictionaries of the statistics of students with indicated health (omitting the latter) present in the spreadsheet, after specifying the file in question.

    Preconditions: file must be a valid file name, health must be a valid integer between 1 and 5, inclusive.

    >>> student_health_list('student-mat.csv', 2)
    [{'School': 'GP', 'Age': 15, 'StudyTime': 2, 'Failures': 0, 'Absences': 0, 'G1': 10, 'G2': 8, 'G3': 9}, {another element},
     …
    ]
    """
    
    dic = {}
    lst = []
    data = open(file, 'r')
    for line in data:
        if line.split(',')[4] == str(health):
            lines = line.strip('\n').split(',')
            dic = {'School': lines[0], 'Age': int(lines[1]), 'StudyTime': float(lines[2]), 'Failures': int(lines[3]),
                   'Absences': int(lines[5]), 'G1': int(lines[6]), 'G2': int(lines[7]), 'G3': int(lines[8])}
            lst.append(dic)

    data.close()

    return lst
#==========================================#
# Place your student_age_list function after this line
def student_age_list(filename: str, age: int) -> list[dict]:
    """Returns a list of student, stored as a dictionary, that have the same 
    specific age. The keys of each dictionary are the 
    
    Preconditions: age > 0
    
    >>> student_age_list('student-mat.csv', 17):
    [{'School': 'GP', 'StudyTime': '2', 'Failures': '0', 'Health': '3', 
    'Absences': '6', 'G1': '5', 'G2': '5', 'G3': '6'}, {another element}, 
    ...
    ]
    """
    list_of_dictionaries = []

    infile = open(filename, "r")
    for line in infile:
        data = line.strip('\n').split(',')
        if data[1] == str(age):
            dictionary = {'School': data[0], 'StudyTime': float(data[2]),
                          'Failures': int(data[3]), 'Health': int(data[4]),
                          'Absences': int(data[5]), 'G1': int(data[6]),
                          'G2': int(data[7]), 'G3': int(data[8])}

            list_of_dictionaries = list_of_dictionaries + [dictionary]
            
    infile.close()

    return list_of_dictionaries


#==========================================#
# Place your student_failures_list function after this line
def student_failures_list(filename: str, fails: int):
    """
    Returns a list of dictionaries. Each dictionary has keys representing each attribute but 'Failures' and the values are the cell values of that attribute in the table that has a given number of failures.

    >>>student_failures_list("student-mat.csv", 3)
    [{'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}, ... {other elements}]
    >>>student_failures_list("student-mat.csv", 4)
    []
    >>>student_failures_list("student-mat.csv", 0)
    [{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, 
    ... {other elements}]
    """
    dic = {}
    lst = []

    with open(filename, 'r') as f:
        data = f.readlines()

    for line in data:
        row = line.strip('\n').split(',')
        if row[3] == str(fails):
            dic = {'School': row[0], 'Age': int(row[1]), 'StudyTime': float(row[2]), 'Health': int(
                row[4]), 'Absences': int(row[5]), 'G1': int(row[6]), 'G2': int(row[7]), 'G3': int(row[8])}

            lst.append(dic)

    f.close()
    return lst


#==========================================#
# Place your load_data function after this line
def load_data(filename: str, filt: tuple) -> list[dict]:
    """
    Function lets user choose which data will be loaded. Takes file name and a 
    tuple containting desired data and value to filter by. Returns list of students
    (stored as dictionaries) where the keys of the dictionary are the labels for 
    all attributes in the spreadsheet except for the attribute in the first 
    item of the tuple.
    
    Preconditions: File must be the correct type. Second tuple value must be valid for whatever it 
    is representing.
    
    >>>load_data('student-mat.csv', ('School', "GP"))
    [{'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 6,
    'G1': 5, 'G2': 6, 'G3': 6},
    {another element},
    ...
    >>>load_data('student-mat.csv', ('Health', 7))
    []    
    """
    school_list = []

    if filt[0] == 'All':
        with open(filename, 'r') as infile:
            infile.readline()
            for line in infile:

                temp_list = line.strip('\n').split(',')

                temp_dict = {
                    "School": str(temp_list[0]),
                    "Age": int(temp_list[1]),
                    "StudyTime": float(temp_list[2]),
                    "Failures": int(temp_list[3]),
                    "Health": int(temp_list[4]),
                    "Absences": int(temp_list[5]),
                    "G1": int(temp_list[6]),
                    "G2": int(temp_list[7]),
                    "G3": int(temp_list[8])
                }
                
                school_list.append(temp_dict)
                
        infile.close()
        return school_list
    
    elif filt[0] == 'School':
        return(student_school_list(filename, filt[1]))
        
    elif filt[0] == 'Age':
        return(student_age_list(filename, filt[1]))

    elif filt[0] == 'Failures':
        return(student_failures_list(filename, filt[1]))
        
    elif filt[0] == 'Health':
        return(student_health_list(filename, filt[1]))

    else:
        return []
#==========================================#
# Place your add_average function after this line
def add_average(stats: list[dict]) -> list[dict]:
    """Return the given list of dictionaries updated with the average grade between G1, G2 and G3 as an extra element.

    Preconditions: stats must be a valid list of dictionaries that include the necessary keys and corresponding values.

    >>> add_average([{'School': 'GP', 'Age': 15, 'StudyTime': 2, 'Failures': 0, 'Absences': 0, 'G1': 10, 'G2': 8, 'G3': 9}])
    [{'School': 'GP', 'Age': 15, 'StudyTime': 2, 'Failures': 0, 'Absences': 0, 'G1': 10, 'G2': 8, 'G3': 9, 'G_Avg': 9.0}]
    >>> add_average([{'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'G1': 10, 'G2': 8, 'G3': 9}, {'School': 'GP', 'Age': 16, 'StudyTime': 1.0,
                'Failures': 0, 'Absences': 4, 'G1': 14, 'G2': 14, 'G3': 14}, {'School': 'GP', 'Age': 16, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 6, 'G1': 13, 'G2': 14, 'G3': 14}])
    [{'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'G1': 10, 'G2': 8, 'G3': 9, 'G_Avg': 9.0}, {'School': 'GP', 'Age': 16, 'StudyTime': 1.0, 'Failures': 0, 'Absences': 4, 'G1': 14, 'G2': 14, 'G3': 14, 'G_Avg': 14.0}, {'School': 'GP', 'Age': 16, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 6, 'G1': 13, 'G2': 14, 'G3': 14, 'G_Avg': 13.67}]
    """
    for dic in stats:
        dic['G_Avg'] = round(((dic['G1'] + dic['G2'] + dic['G3']) / 3), 2)

    return stats
# Do NOT include a main script in your submission