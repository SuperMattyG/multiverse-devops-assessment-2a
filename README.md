# multiverse-devops-assessment-2
This app has been developed for Module 3 Assessment 2 exercise.  This was written by Matthew Gardner.

It takes a file as an argument at runtime.
If results.csv is used it parses the file and outputs the results to clean_results.csv
If clean_results.csv is used the results are printed to std.out

For example:
py survey.py results.csv 
py survey.py clean_results.csv

Unit tests have been created and pytest has been executed against this app.  Pytest reports test coverage as:

test_app.py::test_input_is_list PASSED            [ 10%] 
test_app.py::test_input_is_correct PASSED         [ 20%] 
test_app.py::test_unique_keys PASSED              [ 30%] 
test_app.py::test_answer3_validation PASSED       [ 40%]
test_app.py::test_does_output_exist PASSED        [ 50%] 
test_app.py::test_print_stdout PASSED             [ 60%] 
test_app.py::test_file_exists PASSED              [ 70%] 
test_app.py::test_main_missing_arg PASSED         [ 80%]
test_app.py::test_main_with_arg1 PASSED           [ 90%]
test_app.py::test_main_with_arg2 PASSED           [100%]

---------- coverage: platform win32, python 3.11.2-final-0 -----------
Name                  Stmts   Miss  Cover   Missing
---------------------------------------------------
extract\__init__.py      45      2    96%   58-59
survey.py                25      3    88%   11-13
test_app.py              63      0   100%
---------------------------------------------------
TOTAL                   133      5    96%


The functional requirements were:

#Ticket #1:   Read a CSV file
#Description: In your input script, create a function that will read data from a CSV file.
#Objectives:  The results.csv data file can be successfully processed into an array.
#             Each line of the file is read into a new array item.
#             The file read method must be in a sub-module.

#Ticket #2:     Remove duplicate entries
#Description:   Add functionality to your input script to ignore or remove any duplicate entries
#from the input data.
#Duplicates are based on the User Id field.
#Objectives:    A final array is created with duplicate entries removed.
#               Where duplicates are found, the first entry is retained.

#Ticket #3:     Ignore empty lines
#Description:   Update your input script to ignore any empty lines found when reading in the
#               input data file.
#Objectives:    A final array is created with any empty lines omitted.

#Ticket #2:     Remove duplicate entries
#Description:   Add functionality to your input script to ignore or remove any duplicate entries
#from the input data.
#Duplicates are based on the User Id field.
#Objectives:    A final array is created with duplicate entries removed.
#               Where duplicates are found, the first entry is retained.

#Ticket #5:     Validate the responses to answer 3
#Description:   Update your input script to validate the responses to the third answer field.
#               This answer must have a numeric value between 1 and 10.
#               Any rows with an invalid value are ignored.
#Objectives:    A final array is created with the input data excluding any rows where
#               answer 3 is invalid.
#               No answer 3 values will be outside the range of 1 to 10

#Ticket #6:     Output the cleansed result data to a new file
#Description:   Add functionality to your input script to output the cleansed data to a new CSV
#               file.
#Objectives:    A new file is created called clean_results.csv.
#               The file is recreated on each execution.
#               No invalid or unformatted data is present in the new file.

#Ticket #7:     Create an output script
#Description:   A new output script will be created which reads in the clean_results.csv CSV
#               file and outputs the results to the command line, row by row.
#Objectives:    The script uses the existing sub-module to read the CSV file.
#               The printed output will contain all row data and an appropriate header.
#               Stretch: The printed output will be formatted with fixed length strings.
