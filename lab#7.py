def read_log_file():
    """Asks the user for the file name and returns a list of all the lines in the file.
        if the user imputs a invalid file name they will be alerted and propted to try again"""
    
    while True:
        try:
            file_name = input('Enter the name of the log file: ')
            with open(file_name) as file:
                log_entries = file.readlines()
                return log_entries
            
        except FileNotFoundError:
            print(f"Error: '{file_name}' not found. Please enter a valid file name.")


def process_log_entries(log_entries):
    """Takes the list argument and splits each string inside the list into a lists.
        returns a list of the entries with a status code of 200"""
    
    split_entries = []

    #Splitting every line into a list and appending that list to split_entries
    for element in log_entries:
        entry = element.split()
        split_entries.append(entry)
    
    #Using a list comprehension to filter out the lists that do not have a status code of 200
    processed_data = [split_entries[i] for i in range(len(split_entries)) if split_entries[i][3] == '200']

    return processed_data

def write_processed_data_to_file(processed_data):
    """Creates/opens a file named 'processed_log.txt' and writes all the elements of processed_data to the text file
        formatted by Data, Timestamp, IP Address, Status Code"""

    with open('processed_log.txt', 'w') as file:
        for list in processed_data:
            file.writelines(f'Date: {list[0]}, Timestamp: {list[1]}, IP Address: {list[2]}, Status Code: {list[3]} (OK)\n')
    print("Processed data has been successfully writted to 'processed_log.txt'.")


if __name__ == "__main__":
    #Calling all the functions in sequence. 
    #The interpreter works from the inside out so read_log_file() -> process_log_entries() -> wite_processed_data_to_file()

    write_processed_data_to_file(process_log_entries(read_log_file()))
    