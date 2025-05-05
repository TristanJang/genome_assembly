import glob
from Bio import SeqIO
# Path pattern to FASTA files
FASTA_PATH_PATTERN = "/grp/valafar/data/depot/assembly/sra_nanopore/*/assembly/dnaapler/*.fasta"
# Minimum contig length
MIN_LENGTH = 4000000
# Output file for isolates meeting the criteria
OUTPUT_FILE = "sra_nanopore_complete_assemblies.txt"


def check_contigs(fasta_file, min_length):
    for record in SeqIO.parse(fasta_file, "fasta"):
        if len(record.seq) >= min_length:
            return True
    return False


def main():
    fasta_files = glob.glob(FASTA_PATH_PATTERN)
    total_isolates = len(fasta_files)
    isolates_meeting_criteria = []
    for fasta_file in fasta_files:
        if check_contigs(fasta_file, MIN_LENGTH):
            isolates_meeting_criteria.append(fasta_file)
    # Write isolates meeting criteria to the output file
    with open(OUTPUT_FILE, "w") as output:
        for isolate in isolates_meeting_criteria:
            output.write(f"{isolate}\n")
    # Print summary
    print(f"Total isolates: {total_isolates}")
    print(f"Isolates meeting criteria: {len(isolates_meeting_criteria)}")


if __name__ == "__main__":
    main()
