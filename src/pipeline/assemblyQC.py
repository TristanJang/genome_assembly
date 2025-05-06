import os
import argparse

parser = argparse.ArgumentParser(description="""Performs assembly qc.""")
parser.add_argument("-g", "--genome", required=True, help="Paths to isolate genome")
parser.add_argument("-r", "--reads", required=True, help="Paths to isolate fastq reads")

"""
conda activate varscan
minimap2 -Y --MD -ax map-pb /home/nthosar9846/assembly/hifi/A25_b272_FV_new_flye_assembly/A25_b272_FV_new_fixedstart.fasta /home/nthosar9846/assembly/hifi/A25_b272_FV_new.fastq
samtools sort --output-fmt BAM -o A04_R30124_bsl_new_read_sorted.bam A04_R30124_bsl_new_read_aln.sam
sniffles -m A25_b272_FV_new_read_sorted.bam -v A25_b272_FV_new_sniffles.vcf
"""
args = parser.parse_args()
genome = args.genome
isolate_name = genome.split('/')[-1].split('.')[0]
reads = args.reads
print("Running minimap2 on " + isolate_name + ".................")
minimap2_cmd = "minimap2 -Y --MD -ax map-pb " + genome + " " + reads + "> " + isolate_name + "_read_aln.sam"
os.system(minimap2_cmd)
print("Running samtools on" + isolate_name + ".................")
samtools_cmd = "samtools sort --output-fmt BAM -o "+isolate_name+"_read_sorted.bam " + isolate_name + "_read_aln.sam"
os.system(samtools_cmd)
print("Running sniffles on" + isolate_name + ".................")
sniffles_cmd = "sniffles -m "+isolate_name+"_read_sorted.bam -v "+isolate_name+"_sniffles.vcf"
os.system(sniffles_cmd)
