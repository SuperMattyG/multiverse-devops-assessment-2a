import sys
from extract import get_input, file_exists, capitalize_names, validate, writedata, print_stdout

def get_args():
    try:
        return(sys.argv[1])
    except IndexError:
        print("Please provide 1 argument!\n")
        print("USAGE: [file name]\n")
        raise IndexError
    except:
        print("Unknown Error! See full details below")
        raise

def main():
    filename = get_args() #Get filename for sys arg
    
    if filename != 'clean_results.csv':
        file_exists(filename) # Check if file exists
        final_list = get_input(filename)
        capitalized_list = capitalize_names(final_list)
        validated_list = validate(capitalized_list)
        writedata(validated_list)
    else:
        file_exists(filename) # Check if file exists
        final_list = get_input(filename)
        print_stdout(final_list)

    
if __name__ == '__main__':
    sys.exit(main())