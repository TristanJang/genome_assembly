#!/bin/bash 
#my commands for trycycler runs
#IMPORTANT:
module load python
module load anaconda3
conda activate tools
#also check that thread number used corresponds to CPUs available 
#using trycycler to subsample
mkdir assemblies
trycycler subsample --reads SRR23086718.fastq --genome_size 4.4m --threads 128 --out_dir read_subsets
#generating 12 assemblies using flye,raven and miniasm
#flye:
flye --nano-hq read_subsets/sample_01.fastq --out-dir assembly_01 --threads 128 && cp assembly_01/assembly.fasta assemblies/assembly_01.fasta
flye --nano-hq read_subsets/sample_02.fastq --out-dir assembly_02 --threads 128 && cp assembly_02/assembly.fasta assemblies/assembly_02.fasta
flye --nano-hq read_subsets/sample_03.fastq --out-dir assembly_03 --threads 128 && cp assembly_03/assembly.fasta assemblies/assembly_03.fasta
flye --nano-hq read_subsets/sample_04.fastq --out-dir assembly_04 --threads 128 && cp assembly_04/assembly.fasta assemblies/assembly_04.fasta
#raven:
raven --threads 128 read_subsets/sample_05.fastq > assemblies/assembly_05.fasta
raven --threads 128 read_subsets/sample_06.fastq > assemblies/assembly_06.fasta
raven --threads 128 read_subsets/sample_07.fastq > assemblies/assembly_07.fasta
raven --threads 128 read_subsets/sample_08.fastq > assemblies/assembly_08.fasta
#miniasm+minipolish:
./miniasm_and_minipolish.sh read_subsets/sample_09.fastq 128 > assembly_09.gfa && any2fasta assembly_09.gfa > assemblies/assembly_09.fasta
./miniasm_and_minipolish.sh read_subsets/sample_10.fastq 128 > assembly_10.gfa && any2fasta assembly_10.gfa > assemblies/assembly_10.fasta
./miniasm_and_minipolish.sh read_subsets/sample_11.fastq 128 > assembly_11.gfa && any2fasta assembly_11.gfa > assemblies/assembly_11.fasta
./miniasm_and_minipolish.sh read_subsets/sample_12.fastq 128 > assembly_12.gfa && any2fasta assembly_12.gfa > assemblies/assembly_12.fasta


#clustering contigs
trycycler cluster --assemblies assemblies/*.fasta --reads SRR23086718.fastq --out_dir clusters

