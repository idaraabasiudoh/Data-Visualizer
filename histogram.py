# ECOR 1042 Lab 6 - Individual submission for histogram

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Jonathon Miller"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101287050"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-94"

#==========================================#
# Place your histogram function after this line

import matplotlib.pyplot as plt

def histogram(student_profile: list, plotted_attribute: str) -> None:
    """Function takes a list of dictionaries (student_profile) and a string 
    indicating a specific key/attribute found within the dictionaries of the 
    list. Function displays histogram with the number of students that are at 
    each level or range of levels of the attributes. Categories with a very large number
    of x-axis values are seperated into ranges of levels (whether integer or float values)
    
    Preconditions: student_profile must include a list of dictionaries that 
    have consistent keys. 
    plotted_attribute must be a key within the dictionaries found in the 
    list student_profile
    """
    
    fig1 = plt.figure()

    if plotted_attribute == 'School':
        gp_total = 0
        mb_total = 0
        cf_total = 0
        bd_total = 0
        ms_total = 0
        other_total = 0
        for dic in student_profile:
            if dic['School'] == 'GP':
                gp_total += 1
            elif dic['School'] == 'MB':
                mb_total += 1
            elif dic['School'] == 'CF':
                cf_total += 1
            elif dic['School'] == 'BD':
                bd_total += 1
            else:
                if dic['School'] == 'MS':
                    ms_total += 1

        plt.title('Number of Students Attending Each School')
        plt.xlabel('Schools')
        plt.ylabel('Number of Students')
        plt.bar(['GP', 'MB', 'CF', 'BD', 'MS'], [gp_total, mb_total,
                cf_total, bd_total, ms_total], color='blue')
        plt.show()
            
    elif plotted_attribute == 'Age':
        total_15 = 0
        total_16 = 0
        total_17 = 0
        total_18 = 0
        total_19 = 0
        under_15 = 0
        over_19 = 0
        for dic in student_profile:
            if dic['Age'] == 15:
                total_15 += 1
            elif dic['Age'] == 16:
                total_16 += 1
            elif dic['Age'] == 17:
                total_17 += 1
            elif dic['Age'] == 18:
                total_18 += 1
            elif dic['Age'] == 19:
                total_19 += 1
            elif dic['Age'] < 15:
                under_15 += 1
            else:
                if dic['Age'] > 19:
                    over_19 += 1
        plt.title('Number of Students by Age')
        plt.xlabel('Age (Years)')
        plt.ylabel('Number of Students')
        plt.bar(['< 15', '15', '16', '17', '18', '19', '> 19'], [under_15, total_15,
                total_16, total_17, total_18, total_19, over_19], color="blue")
        plt.show()

    elif plotted_attribute == 'StudyTime':
        total_1 = 0
        total_2 = 0
        total_3 = 0
        total_4 = 0
        total_5 = 0
        over_5 = 0
        total_0 = 0
        for dic in student_profile:
            if dic['StudyTime'] == 1.0:
                total_1 += 1
            elif dic['StudyTime'] == 2.0:
                total_2 += 1
            elif dic['StudyTime'] == 3.0:
                total_3 += 1
            elif dic['StudyTime'] == 4.0:
                total_4 += 1
            elif dic['StudyTime'] == 5.0:
                total_5 += 1
            elif dic['StudyTime'] == 0:
                total_0 += 1
            else:
                if dic['StudyTime'] > 5.0:
                    over_5 += 1
        plt.title('Number of Students by Study Time')
        plt.xlabel('Study Time')
        plt.ylabel('Numer of Students')
        plt.bar(['0.0', '1.0', '2.0', '3.0', '4.0', '5.0', '>5.0'], [
                total_0, total_1, total_2, total_3, total_4, total_5, over_5], color='blue')
        plt.show()

    elif plotted_attribute == 'Failures':
        total_0 = 0
        total_1 = 0
        total_2 = 0
        total_3 = 0
        total_4plus = 0
        for dic in student_profile:
            if dic['Failures'] == 0:
                total_0 += 1
            elif dic['Failures'] == 1:
                total_1 += 1
            elif dic['Failures'] == 2:
                total_2 += 1
            elif dic['Failures'] == 3:
                total_3 += 1
            else:
                if dic['Failures'] >= 4:
                    total_4plus += 1
        plt.title('Number of Students by Failures')
        plt.xlabel('Total Failures')
        plt.ylabel('Number of Students')
        plt.bar(['0', '1', '2', '3', '4+'], [total_0, total_1,
                total_2, total_3, total_4plus], color='blue')
        plt.show()

    elif plotted_attribute == 'Health':
        total_0 = 0
        total_1 = 0
        total_2 = 0
        total_3 = 0
        total_4 = 0
        total_5 = 0
        total_6plus = 0
        for dic in student_profile:
            if dic['Health'] == 0:
                total_0 += 1
            elif dic['Health'] == 1:
                total_1 += 1
            elif dic['Health'] == 2:
                total_2 += 1
            elif dic['Health'] == 3:
                total_3 += 1
            elif dic['Health'] == 4:
                total_4 += 1
            elif dic['Health'] == 5:
                total_5 += 1
            else:
                if dic['Health'] >= 6:
                    total_6plus += 1
        plt.title('Number of Students by Health')
        plt.xlabel('Health Score')
        plt.ylabel('Number of Students')
        plt.bar(['0', '1', '2', '3', '4', '5', '6+'], [total_0, total_1,
                total_2, total_3, total_4, total_5, total_6plus], color='blue')
        plt.show()

    elif plotted_attribute == 'Absences':
        total_0 = 0
        total_1to5 = 0
        total_6to10 = 0
        total_11to15 = 0
        total_16to20 = 0
        total_21to25 = 0
        total_26to30 = 0
        total_31to35 = 0
        total_36plus = 0
        for dic in student_profile:
            if dic['Absences'] == 0:
                total_0 += 1
            elif 1 <= dic['Absences'] <= 5:
                total_1to5 += 1
            elif 6 <= dic['Absences'] <= 10:
                total_6to10 += 1
            elif 11 <= dic['Absences'] <= 15:
                total_11to15 += 1
            elif 16 <= dic['Absences'] <= 20:
                total_16to20 += 1
            elif 21 <= dic['Absences'] <= 25:
                total_21to25 += 1
            elif 26 <= dic['Absences'] <= 30:
                total_26to30 += 1
            elif 31 <= dic['Absences'] <= 35:
                total_31to35 += 1
            else:
                if dic['Absences'] >= 36:
                    total_36plus += 1
        plt.title('Number of Students by Absences')
        plt.xlabel('Number of Absences')
        plt.ylabel('Number of Students')
        plt.bar(['0', '1-5', '6-10', '11-15', '16-20', '21-25', '26-30', '31-35', '36+'],
                [total_0, total_1to5, total_6to10, total_11to15, total_16to20, total_21to25,
                 total_26to30, total_31to35, total_36plus], color='blue')
        plt.show()

    elif plotted_attribute == 'G1':
        total_0 = 0
        total_1to5 = 0
        total_6to10 = 0
        total_11to15 = 0
        total_16to20 = 0
        total_21plus = 0
        for dic in student_profile:
            if dic['G1'] == 0:
                total_0 += 1
            elif 1 <= dic['G1'] <= 5:
                total_1to5 += 1
            elif 6 <= dic['G1'] <= 10:
                total_6to10 += 1
            elif 11 <= dic['G1'] <= 15:
                total_11to15 += 1
            elif 16 <= dic['G1'] <= 20:
                total_16to20 += 1
            else:
                if dic['G1'] >= 21:
                    total_21plus += 1
        plt.title('Number of Students by G1 Score')
        plt.xlabel('G1 Score')
        plt.ylabel('Number of Students')
        plt.bar(['0', '1-5', '6-10', '11-15', '16-20', '21+'], [total_0, total_1to5,
                total_6to10, total_11to15, total_16to20, total_21plus], color='blue')
        plt.show()
        
    elif plotted_attribute == 'G2':
        total_0 = 0
        total_1to5 = 0
        total_6to10 = 0
        total_11to15 = 0
        total_16to20 = 0
        total_21plus = 0
        for dic in student_profile:
            if dic['G2'] == 0:
                total_0 += 1
            elif 1 <= dic['G2'] <= 5:
                total_1to5 += 1
            elif 6 <= dic['G2'] <= 10:
                total_6to10 += 1
            elif 11 <= dic['G2'] <= 15:
                total_11to15 += 1
            elif 16 <= dic['G2'] <= 20:
                total_16to20 += 1
            else:
                if dic['G2'] >= 21:
                    total_21plus += 1
        plt.title('Number of Students by G2 Score')
        plt.xlabel('G2 Score')
        plt.ylabel('Number of Students')
        plt.bar(['0', '1-5', '6-10', '11-15', '16-20', '21+'], [total_0, total_1to5,
                total_6to10, total_11to15, total_16to20, total_21plus], color='blue')
        plt.show()
        
    elif plotted_attribute == 'G3':
        total_0 = 0
        total_1to5 = 0
        total_6to10 = 0
        total_11to15 = 0
        total_16to20 = 0
        total_21plus = 0
        for dic in student_profile:
            if dic['G3'] == 0:
                total_0 += 1
            elif 1 <= dic['G3'] <= 5:
                total_1to5 += 1
            elif 6 <= dic['G3'] <= 10:
                total_6to10 += 1
            elif 11 <= dic['G3'] <= 15:
                total_11to15 += 1
            elif 16 <= dic['G3'] <= 20:
                total_16to20 += 1
            else:
                if dic['G3'] >= 21:
                    total_21plus += 1
        plt.title('Number of Students by G3 Score')
        plt.xlabel('G3 Score')
        plt.ylabel('Number of Students')
        plt.bar(['0', '1-5', '6-10', '11-15', '16-20', '21+'], [total_0, total_1to5,
                total_6to10, total_11to15, total_16to20, total_21plus], color='blue')
        plt.show()

    elif plotted_attribute == 'G_Avg':
        total_0 = 0
        total_1to5 = 0
        total_6to10 = 0
        total_11to15 = 0
        total_16to20 = 0
        total_21plus = 0
        for dic in student_profile:
            if dic['G_Avg'] == 0:
                total_0 += 1
            elif 1 <= dic['G_Avg'] <= 5:
                total_1to5 += 1
            elif 6 <= dic['G_Avg'] <= 10:
                total_6to10 += 1
            elif 11 <= dic['G_Avg'] <= 15:
                total_11to15 += 1
            elif 16 <= dic['G_Avg'] <= 20:
                total_16to20 += 1
            else:
                if dic['G_Avg'] >= 21:
                    total_21plus += 1
        plt.title('Number of Students by G_Avg Score')
        plt.xlabel('G_Avg Score')
        plt.ylabel('Number of Students')
        plt.bar(['0', '1-5', '6-10', '11-15', '16-20', '21+'], [total_0, total_1to5,
                total_6to10, total_11to15, total_16to20, total_21plus], color='blue')
        plt.show()
    

            
                
            
        








#Do NOT include a main script in your submission
