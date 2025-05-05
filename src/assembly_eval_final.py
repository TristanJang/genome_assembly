import glob
from Bio import SeqIO
# Path pattern to your FASTA files (wildcards allowed)
FASTA_PATH_PATTERN = "/grp/valafar/data/depot/assembly/sra_pacbio/*/assembly/dnaapler/*.fasta"
# Minimum contig length in bases
MIN_LENGTH = 4000000
# Output file for isolates meeting the criteria
OUTPUT_FILE = "pacbio_sra_complete_final.txt"


def check_single_contig(fasta_file, min_length):
    """
    Check if the FASTA file contains exactly one contig and that the contig is at least min_length bases long.
    """
    contigs = list(SeqIO.parse(fasta_file, "fasta"))
    if len(contigs) <= 4 and len(contigs[0].seq) >= min_length:
        return True
    return False


def main():
    """
    Main function to process all FASTA files matching the pattern, check for a single contig of sufficient length,
    and output results to a text file.
    """
    # Get the list of FASTA files matching the wildcard pattern
    fasta_files = glob.glob(FASTA_PATH_PATTERN)
    total_isolates = len(fasta_files)
    isolates_meeting_criteria = []
    for fasta_file in fasta_files:
        if check_single_contig(fasta_file, MIN_LENGTH):
            isolates_meeting_criteria.append(fasta_file)
    # Write isolates meeting criteria to the output file
    with open(OUTPUT_FILE, "w") as output:
        for isolate in isolates_meeting_criteria:
            parts = isolate.strip().split('/')
            srr_identifier = parts[7]
            output.write(f"{srr_identifier}\n")
    # Print summary
    print(f"Total isolates: {total_isolates}")
    print(f"Isolates meeting criteria: {len(isolates_meeting_criteria)}")


if __name__ == "__main__":
    main()
