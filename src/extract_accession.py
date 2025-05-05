def extract_srr_identifiers(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Split the line by '/' and get the 7th element (index 6)
            parts = line.strip().split('/')
            srr_identifier = parts[7]
            outfile.write(srr_identifier + '\n')
# Usage example
input_file = 'nanopore_sra_single_contig_path.txt'
output_file = 'nanopore_sra_single_contig.txt'
extract_srr_identifiers(input_file, output_file)