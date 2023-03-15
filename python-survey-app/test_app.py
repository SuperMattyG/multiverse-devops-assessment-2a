#Author:      Matthew Gardner
import os, subprocess

from extract import get_input, capitalize_names, validate, writedata, print_stdout, file_exists

#Ticket #1:   Read a CSV file
#Description: In your input script, create a function that will read data from a CSV file.
#Objectives:  The results.csv data file can be successfully processed into an array.
#             Each line of the file is read into a new array item.
#             The file read method must be in a sub-module.

def test_input_is_list():
    #Arrange
    filename = "results.csv"
    expected_output = list

    #Act
    output = get_input(filename)

    #Assert
    assert type(output) == expected_output
    return

def test_input_is_correct():
    #Arrange
    filename = "results.csv"
    expected_output = {'user_id': '1', 'first_name': 'Charissa', 'last_name': 'Clark', 'answer_1': 'yes', 'answer_2': 'c', 'answer_3': '7'}
    
    #Act
    output = get_input(filename)
    output_first_line = output[0]

    #Assert
    assert output_first_line == expected_output
    return


#Ticket #2:     Remove duplicate entries
#Description:   Add functionality to your input script to ignore or remove any duplicate entries
#from the input data.
#Duplicates are based on the User Id field.
#Objectives:    A final array is created with duplicate entries removed.
#               Where duplicates are found, the first entry is retained.

def test_unique_keys():
    #Arrange
    filename = "results.csv"
    expected_output = 20

    #Act
    output = get_input(filename)

    #Assert
    assert len(output) == expected_output
    return

#Ticket #5:     Validate the responses to answer 3
#Description:   Update your input script to validate the responses to the third answer field.
#               This answer must have a numeric value between 1 and 10.
#               Any rows with an invalid value are ignored.
#Objectives:    A final array is created with the input data excluding any rows where
#               answer 3 is invalid.
#               No answer 3 values will be outside the range of 1 to 10

def test_answer3_validation():
    #Arrange
    filename = "results.csv"
    final_list = get_input(filename)
    capitalized_list = capitalize_names(final_list)
    i = 0

    #Act
    output = validate(capitalized_list)

    #Assert
    for row in output:
        assert int(output[i]['answer_3']) > 1 and int(output[i]['answer_3']) <= 10
        i = i + 1
    return

#Ticket #6:     Output the cleansed result data to a new file
#Description:   Add functionality to your input script to output the cleansed data to a new CSV
#               file.
#Objectives:    A new file is created called clean_results.csv.
#               The file is recreated on each execution.
#               No invalid or unformatted data is present in the new file.

def test_does_output_exist():
    #Arrange
    final_list = get_input("results.csv")
    capitalized_list = capitalize_names(final_list)
    validated_list = validate(capitalized_list)
        
    #Act
    writedata(validated_list)

    #Assert
    assert os.path.exists(os.path.join("clean_results.csv"))
    return

#Ticket #7:     Create an output script
#Description:   A new output script will be created which reads in the clean_results.csv CSV
#               file and outputs the results to the command line, row by row.
#Objectives:    The script uses the existing sub-module to read the CSV file.
#               The printed output will contain all row data and an appropriate header.
#               Stretch: The printed output will be formatted with fixed length strings.

def test_print_stdout():
    #Arrange
    final_list = get_input("clean_results.csv")
    expected_output = type(print_stdout(final_list))

    #Act
    output = dict

    #Assert
    assert expected_output == output
    return

def test_file_exists():
    #Arrange
    filename = "testfile.csv"
    expected_output = file_exists(filename)

    with open("testfile.csv", "r") as f:
        expected_output = f.read()
    assert expected_output == "1,2,3"

    return

def test_main_missing_arg():
    result = subprocess.run(["python", "survey.py"], capture_output=True, text=True)
    assert "Please provide 1 argument" in result.stdout
    return

def test_main_with_arg1():
    result = subprocess.run(["python", "survey.py", "results.csv"], capture_output=True, text=True)
    assert "" in result.stdout
    return

def test_main_with_arg2():
    result = subprocess.run(["python", "survey.py", "clean_results.csv"], capture_output=True, text=True)
    assert "" in result.stdout
    return