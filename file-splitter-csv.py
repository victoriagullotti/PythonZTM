import csv

csv_file = r"C:\Users\Guest1\Desktop\code\PythonZTM\auto-parts.csv"

max_lines_per_file = 100        # Maximum number of lines per file


# Open the CSV file
with open(csv_file, 'r') as input_file:
    csv_reader = csv.reader(input_file)

    # Skip the header row if there is one
    header_row = next(csv_reader, None)

    # Initialize variables for tracking the current output file and lines written
    current_output_file = None
    lines_written = 0

    # Loop through each row
    for row in csv_reader:
        # Create a new output file if necessary
        if current_output_file is None or lines_written >= max_lines_per_file:
            
            # Close the current file if we have one
            if current_output_file is not None:
                current_output_file.close()
            
            file_num = lines_written // max_lines_per_file + 1
            current_output_file = open(f'output_file_{file_num}.csv', 'w', newline='')
            csv_writer = csv.writer(current_output_file)
            
            # Insert the header row ONLY if the is one
            if header_row is not None:
                csv_writer.writerow(header_row)
            lines_written = 0

        # Write the row to the current output file
        csv_writer.writerow(row)
        lines_written += 1

    # Close the final output file
    if current_output_file is not None:
        current_output_file.close()
