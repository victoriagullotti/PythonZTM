import csv

#Input the csv file path
csv_file = input('csv file: ')

# Open the CSV file
with open(csv_file, 'r') as input_file:
    csv_reader = csv.reader(input_file)

    # Skip the header row if there is one
    header_row = next(csv_reader, None)

    part_numbers = []
    part_numbers_duplicates = []

    for row in csv_reader:
        #print(row[0])

        # Check if the part number is already in the list
        if row[0] in part_numbers:
            part_numbers_duplicates.append(row[0])      # Its a duplicate!!!
        else:    
            part_numbers.append(row[0])                 # Add the part number to the list
    
    print('Duplicates: ', part_numbers_duplicates)