# ECOR 1042 Lab 4 - team submission

#import check module here
import check
#import load_data module here
import load_data
# Update "" with your the name of the active members of the team
__author__ = "Madhav Ajish, Roman Britto, Idara-Udoh Abasi, Jonathon Miller"

# Update "" with your student number (e.g., 100100100)

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-94"

#==========================================#

# Place test_return_list function here 
def test_return_list():
    #Complete the function with your test cases
    
    #test that student_school_list returns a list (3 different test cases required)
    check.equal(isinstance(load_data.student_school_list("student-test.csv", "test"), list), True)
    check.equal(isinstance(load_data.student_school_list("student-test.csv", "GP"), list), True)
    check.equal(isinstance(load_data.student_school_list("student-test.csv", ""), list), True)
    # test that student_age_list returns a list (3 different test cases required)
    check.equal(isinstance(load_data.student_age_list("student-test.csv", 1), list), True)
    check.equal(isinstance(load_data.student_age_list("student-test.csv", 17), list), True)
    check.equal(isinstance(load_data.student_age_list("student-test.csv", 100), list), True)
    # test that student_health_list returns a list (3 different test cases required)
    check.equal(isinstance(load_data.student_health_list("student-test.csv", 3), list), True)
    check.equal(isinstance(load_data.student_health_list("student-test.csv", 5), list), True)
    check.equal(isinstance(load_data.student_health_list("student-test.csv", 0), list), True)
    # test that student_failures_list returns a list (3 different test cases required)
    check.equal(isinstance(load_data.student_failures_list("student-test.csv", 3), list), True)
    check.equal(isinstance(load_data.student_failures_list("student-test.csv", 4), list), True)
    check.equal(isinstance(load_data.student_failures_list("student-test.csv", 0), list), True)
    # test that load_data returns a list (6 different test cases required)
    check.equal(isinstance(load_data.load_data("student-test.csv", ("School", "MB")), list), True)
    check.equal(isinstance(load_data.load_data("student-test.csv", ("Health", 2)), list), True)
    check.equal(isinstance(load_data.load_data("student-test.csv", ("Failures", 2)), list), True)
    check.equal(isinstance(load_data.load_data("student-test.csv", ("Age", 18)), list), True)
    check.equal(isinstance(load_data.load_data("student-test.csv", ("All", 15)), list), True)
    check.equal(isinstance(load_data.load_data("student-test.csv", ("All", "")), list), True)
    # test that add_average returns a list (3 different test cases required)
    check.equal(isinstance(load_data.add_average(load_data.load_data("student-test.csv", ("Failures", 5))), list), True)
    check.equal(isinstance(load_data.add_average(load_data.load_data("student-test.csv", ("School", "MS"))), list), True)
    check.equal(isinstance(load_data.add_average(load_data.load_data("student-test.csv", ("All", 5))), list), True)
    
    check.summary()

# Place test_return_list_correct_lenght function here

def test_return_list_correct_lenght():
    #Complete the function with your test cases
    
    #test that student_school_list returns a list with the correct lenght (3 different test cases required)
    check.equal(len(load_data.student_school_list('student-test.csv', 'GP')), 3)
    check.equal(len(load_data.student_school_list('student-test.csv', 'XS')), 0)
    check.equal(len(load_data.student_school_list('student-test.csv', 'MB')), 2)

    # test that student_age_list returns a list  with the correct lenght (3 different test cases required)
    check.equal(len(load_data.student_age_list('student-test.csv', 17)), 6)
    check.equal(len(load_data.student_age_list('student-test.csv', 15)), 3)
    check.equal(len(load_data.student_age_list('student-test.csv', 27)), 0)
    

    # test that student_health_list returns a list  with the correct lenght (3 different test cases required)
    check.equal(len(load_data.student_health_list('student-test.csv', 3)), 8)
    check.equal(len(load_data.student_health_list('student-test.csv', 5)), 3)
    check.equal(len(load_data.student_health_list('student-test.csv', 19)), 0)


    # test that student_failures_list returns a list   with the correct lenght(3 different test cases required)
    check.equal(len(load_data.student_failures_list('student-test.csv', 0)), 11)
    check.equal(len(load_data.student_failures_list('student-test.csv', 3)), 1)
    check.equal(len(load_data.student_failures_list('student-test.csv', 99)), 0)


    # test that load_data returns a list  with the correct lenght (6 different test cases required)
    check.equal(len(load_data.load_data('student-test.csv', ('School', 'GP'))), 3)
    check.equal(len(load_data.load_data('student-test.csv', ('Age', 16))), 2)
    check.equal(len(load_data.load_data('student-test.csv', ('Failures', 3))), 1)
    check.equal(len(load_data.load_data('student-test.csv', ('Health', 4))), 3)
    check.equal(len(load_data.load_data('student-test.csv', ('Age', 4))), 0)
    check.equal(len(load_data.load_data('student-test.csv', ('All', 3))), 15)

     # test that add_average returns a list   with the correct lenght (3 different test cases required)
    check.equal(len(load_data.add_average(load_data.load_data('student-test.csv', ('Invalid entry', 'MB')))), 0)
    check.equal(len(load_data.add_average(load_data.load_data('student-test.csv', ('Age', 15)))), 3)
    check.equal(len(load_data.add_average(load_data.load_data('student-test.csv', ('Failures', 0)))), 11)
    

    check.summary()


#Place test_return_correct_dict_inside_list function here

def test_return_correct_dict_inside_list():
    # Complete the function with your test cases

    # test that student_school_list returns a correct dictionary inside the list (3 different test cases required)
    check.equal({'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6,
                'G1': 5, 'G2': 6, 'G3': 6}, load_data.student_school_list('student-test.csv', 'GP')[0])

    check.equal({'Age': 15, 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10,
                'G1': 7, 'G2': 8, 'G3': 10}, load_data.student_school_list('student-test.csv', 'GP')[2])

    check.within(2.0, load_data.student_school_list(
        'student-test.csv', 'GP')[1]['StudyTime'], 0.001)

    # test that student_age_list returns a correct dictionary inside the list  (3 different test cases required)
    check.equal({'School': 'GP', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6,
                'G1': 5, 'G2': 6, 'G3': 6}, load_data.student_age_list('student-test.csv', 18)[0])

    check.equal({'School': 'MS', 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 2,
                'G1': 9, 'G2': 8, 'G3': 8}, load_data.student_age_list('student-test.csv', 18)[3])

    check.within(2.0, load_data.student_age_list(
        'student-test.csv', 18)[0]['StudyTime'], 0.001)

    # test that student_health_list returns a correct dictionary inside the list  (3 different test cases required)
    check.equal({'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 6,
                'G1': 5, 'G2': 6, 'G3': 6}, load_data.student_health_list('student-test.csv', 3)[0])

    check.equal({'School': 'BD', 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 1,
                'G1': 13, 'G2': 12, 'G3': 12}, load_data.student_health_list('student-test.csv', 3)[7])

    check.within(3.0, load_data.student_health_list(
        'student-test.csv', 3)[7]['StudyTime'], 0.001)

    # test that student_failures_list returns a correct dictionary inside the list (3 different test cases required)
    check.equal({'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Health': 3, 'Absences': 6,
                'G1': 5, 'G2': 6, 'G3': 6}, load_data.student_failures_list('student-test.csv', 0)[0])

    check.equal({'School': 'MS', 'Age': 18, 'StudyTime': 3.0, 'Health': 5, 'Absences': 2,
                'G1': 9, 'G2': 8, 'G3': 8}, load_data.student_failures_list('student-test.csv', 0)[10])

    check.within(3.0, load_data.student_failures_list(
        'student-test.csv', 0)[10]['StudyTime'], 0.001)

    # test that load_data returns a correct dictionary inside the list (6 different test cases required)
    check.equal({'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6,
                'G1': 5, 'G2': 6, 'G3': 6}, load_data.load_data('student-test.csv', ('School', "GP"))[0])

    check.equal({'School': 'GP', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6,
                'G1': 5, 'G2': 6, 'G3': 6}, load_data.load_data('student-test.csv', ('Age', 18))[0])

    check.equal({'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 6,
                'G1': 5, 'G2': 6, 'G3': 6}, load_data.load_data('student-test.csv', ('Health', 3))[0])

    check.equal({'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Health': 3, 'Absences': 10,
                'G1': 7, 'G2': 8, 'G3': 10}, load_data.load_data('student-test.csv', ('Failures', 3))[0])

    check.within(3.0, load_data.load_data(
        'student-test.csv', ('Health', 4))[0]['StudyTime'], 0.001)

    check.within(2.0, load_data.load_data('student-test.csv',
                 ('Health', 3))[2]['StudyTime'], 0.001)

    # test that add_average returns a lcorrect dictionary inside the list  (3 different test cases required)
    check.equal({'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'G1': 10, 'G2': 8, 'G3': 9, 'G_Avg': 9.0}, load_data.add_average([{'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'G1': 10, 'G2': 8, 'G3': 9}, {'School': 'GP', 'Age': 16, 'StudyTime': 1.0,
                                                                                                                                                                                                                                                                        'Failures': 0, 'Absences': 4, 'G1': 14, 'G2': 14, 'G3': 14}, {'School': 'GP', 'Age': 16, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 6, 'G1': 13, 'G2': 14, 'G3': 14}])[0])

    check.equal({'School': 'GP', 'Age': 16, 'StudyTime': 1.0, 'Failures': 0, 'Absences': 4, 'G1': 14, 'G2': 14, 'G3': 14, 'G_Avg': 14.0}, load_data.add_average([{'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'G1': 10, 'G2': 8, 'G3': 9}, {'School': 'GP', 'Age': 16, 'StudyTime': 1.0,
                                                                                                                                                                                                                                                                           'Failures': 0, 'Absences': 4, 'G1': 14, 'G2': 14, 'G3': 14}, {'School': 'GP', 'Age': 16, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 6, 'G1': 13, 'G2': 14, 'G3': 14}])[1])

    check.within(14.0, load_data.add_average([{'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'G1': 10, 'G2': 8, 'G3': 9}, {'School': 'GP', 'Age': 16, 'StudyTime': 1.0,
                                                                                                                                                        'Failures': 0, 'Absences': 4, 'G1': 14, 'G2': 14, 'G3': 14}, {'School': 'GP', 'Age': 16, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 6, 'G1': 13, 'G2': 14, 'G3': 14}])[1]['G_Avg'], 0.001)

    check.summary()


#Place test_add_average function here

def test_add_average():
    # Complete the function with your test cases

    # test that the function does not change the lengh of the list provided as input parameter (5 different test cases required)
    check.equal(len(load_data.add_average(load_data.load_data('student-test.csv', ('School', 'BD')))),
                len(load_data.load_data('student-test.csv', ('School', 'BD'))))   # school
    check.equal(len(load_data.add_average(load_data.load_data('student-test.csv', ('Health', '3')))),
                len(load_data.load_data('student-test.csv', ('Health', '3'))))   # health
    check.equal(len(load_data.add_average(load_data.load_data('student-test.csv', ('Age', '15')))),
                len(load_data.load_data('student-test.csv', ('Age', '15'))))   # age
    check.equal(len(load_data.add_average(load_data.load_data('student-test.csv', ('Failures', 0)))),
                len(load_data.load_data('student-test.csv', ('Failures', 0))))   # failures
    check.equal(len(load_data.add_average(load_data.load_data('student-test.csv', ('All', 5)))),
                len(load_data.load_data('student-test.csv', ('All', 5))))   # all

    # test that the length of the list returned by the function is the length of an empty list when it is called with an empty list
    check.equal(len(load_data.add_average([])), 0)

    # test that the function inscrememnts the number of keys of the dictionary inside the list by one  (5 different test cases required)
    check.equal(len((load_data.add_average(load_data.load_data('student-test.csv', ('School', 'BD'))))[0].keys()),
                len((load_data.load_data('student-test.csv', ('School', 'BD')))[0].keys()) + 1)   # school
    check.equal(len((load_data.add_average(load_data.load_data('student-test.csv', ('Health', 3))))[0].keys()),
                len((load_data.load_data('student-test.csv', ('Health', 3)))[0].keys()) + 1)   # health
    check.equal(len((load_data.add_average(load_data.load_data('student-test.csv', ('Age', '15'))))[0].keys()),
                len((load_data.load_data('student-test.csv', ('Age', '15')))[0].keys()) + 1)   # age
    check.equal(len((load_data.add_average(load_data.load_data('student-test.csv', ('Failures', 0))))[0].keys()),
                len((load_data.load_data('student-test.csv', ('Failures', 0)))[0].keys()) + 1)   # failures
    check.equal(len((load_data.add_average(load_data.load_data('student-test.csv', ('All', 5))))[0].keys()),
                len((load_data.load_data('student-test.csv', ('All', 5)))[0].keys()) + 1)   # all

    # test that the G_Avg value is properly calculated  (5 different test cases required)
    check.equal(load_data.add_average(load_data.load_data('student-test.csv',
                ('School', 'BD')))[0].get('G_Avg'), 8.0)   # school
    check.equal(load_data.add_average(load_data.load_data('student-test.csv',
                ('Health', 3)))[0].get('G_Avg'), 5.67)     # health
    check.equal(load_data.add_average(load_data.load_data('student-test.csv',
                ('Age', '15')))[2].get('G_Avg'), 7.0)      # age
    check.equal(load_data.add_average(load_data.load_data('student-test.csv',
                ('Failures', 0)))[-1].get('G_Avg'), 8.33)  # failures
    check.equal(load_data.add_average(
        load_data.load_data('student-test.csv', ('All', 5)))[0].get('G_Avg'), 5.67)  # all

    check.summary()


# Do NOT include a main script in your submission
if __name__ == "__main__":
    test_return_list()
    test_return_list_correct_lenght()
    test_add_average()
    test_return_correct_dict_inside_list()