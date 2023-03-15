import csv
#Author: matthew Gardner

#def get_input() - Covers this Ticket
#Ticket #1:   Read a CSV file
#Description: In your input script, create a function that will read data from a CSV file.
#Objectives:  The results.csv data file can be successfully processed into an array.
#             Each line of the file is read into a new array item.
#             The file read method must be in a sub-module.

#def get_input() - Covers this Ticket
#Ticket #2:     Remove duplicate entries
#Description:   Add functionality to your input script to ignore or remove any duplicate entries
#from the input data.
#Duplicates are based on the User Id field.
#Objectives:    A final array is created with duplicate entries removed.
#               Where duplicates are found, the first entry is retained.

#def get_input() - Covers this Ticket
#Ticket #3:     Ignore empty lines
#Description:   Update your input script to ignore any empty lines found when reading in the
#               input data file.
#Objectives:    A final array is created with any empty lines omitted.

def get_input(filename):

    #Initialise list that values will be appneded to
    cleansed_list=[]

    with open(filename, 'r') as f: #Open the input file
        
        #Read the CSV file into a list of dictionaries
        #Ticket #1
        reader = csv.DictReader(f)
        
        #Create a set to store unique values
        #Ticket #2
        unique_values = set()

        #Iterate over each row in the input file
        for row in reader:
            #Get the value of the field to check for duplicates
            field_value = row ['user_id']
            
            #If the value has not already been seen, add it to the set and write the row to the output file
            if field_value not in unique_values:
                #Ticket #3: If statement to cover off Ticket 3.  Will ignore empty lines
                if len(field_value) > 0:
                    unique_values.add(field_value)
                    cleansed_list.append(row)
    
    return list(cleansed_list)

#Checks if file exists
def file_exists(filename):
    try:
        open(filename)
    except FileNotFoundError:
        print("File not found")
    return


#Ticket #4:     Capitalise user name fields
#Description:   Add functionality to your input script to automatically capitalise the first_name
#               and last_name fields found in the input data.
#Objectives:    All names are capitalised in all data entries

def capitalize_names(lowercase_list):

    for item in lowercase_list:
        item['first_name'] = item['first_name'].capitalize()
        item['last_name'] = item['last_name'].capitalize()

    return list(lowercase_list)


#Ticket #5:     Validate the responses to answer 3
#Description:   Update your input script to validate the responses to the third answer field.
#               This answer must have a numeric value between 1 and 10.
#               Any rows with an invalid value are ignored.
#Objectives:    A final array is created with the input data excluding any rows where
#               answer 3 is invalid.
#               No answer 3 values will be outside the range of 1 to 10

def validate(input_list):

    validated_list = []

    for item in input_list:
        if int(item['answer_3']) >= 1 and int(item['answer_3']) <= 10:
            validated_list.append(item)
            
    return list(validated_list)

#Ticket #6:     Output the cleansed result data to a new file
#Description:   Add functionality to your input script to output the cleansed data to a new CSV
#               file.
#Objectives:    A new file is created called clean_results.csv.
#               The file is recreated on each execution.
#               No invalid or unformatted data is present in the new file.

def writedata(final_list):

    filename = 'clean_results.csv'  #Define the file name
    headers = ['user_id', 'first_name', 'last_name', 'answer_1', 'answer_2', 'answer_3'] #set the headers

    with open(filename, 'w', newline = '') as file: #Open the file for writing(w)
        writer = csv.DictWriter(file, fieldnames=headers)   #Create a csv writer
        writer.writeheader()    #Write the header row

        #Write each row with data
        for row in final_list:
            writer.writerow(row)

    return

#Ticket #7:     Create an output script
#Description:   A new output script will be created which reads in the clean_results.csv CSV
#               file and outputs the results to the command line, row by row.
#Objectives:    The script uses the existing sub-module to read the CSV file.
#               The printed output will contain all row data and an appropriate header.
#               Stretch: The printed output will be formatted with fixed length strings.

def print_stdout(final_list):
    
    length=30
    #':<' specifies that the string should be left justifiedand the number specified the length
    print(f'{"user_id":<{length}}',f'{"first_name":<{length}}',f'{"last_name":<{length}}',f'{"answer_1":<{length}}',f'{"answer_2":<{length}}',f'{"answer_3":<{length}}',)

    for item in final_list:
        print(f'{item["user_id"]:<{length}}',f'{item["first_name"]:<{length}}',f'{item["last_name"]:<{length}}',f'{item["answer_1"]:<{length}}',f'{item["answer_2"]:<{length}}',f'{item["answer_3"]:<{length}}',)
    return item