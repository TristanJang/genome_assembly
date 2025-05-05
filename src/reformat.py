
import csv

input_file = 'lineages.tsv'
output_file = 'lineages_new.tsv'

# Open the input and output TSV files
with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile, delimiter='\t')
    writer = csv.writer(outfile, delimiter='\t')

    # Initialize a variable to keep track of the current row number
    row_num = 0

    # Iterate through the rows in the input file
    for row in reader:
        if row_num == 0:
            writer.writerow(row)
        # Check if the row number is even (assuming the first row has index 0)
        elif row_num % 2 == 1:
            writer.writerow(row)  # Write the row to the output file
        row_num += 1

