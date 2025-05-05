#!/bin/bash
t=128 #number of threads
isolate_reads=SRR23086718.fastq
module load python
module load anaconda3 
conda activate tools
#step 3 reconciling contigs, only to be done after manually going through every cluster and removing all "bad" clusters
#following commands to be done for each cluster
trycycler reconcile --reads reads.fastq --cluster_dir clusters/cluster_001 --threads $t --verbose
#trycycler reconcile --reads reads.fastq --cluster_dir clusters/cluster_007 --threads $t --verbose
#results in 2_all_seqs.fasta for each cluster

#step 4 Multiple sequence alignment
#also to be done for each cluster
trycycler msa --cluster_dir clusters/cluster_001 --threads $t
#trycycler msa --cluster_dir clusters/cluster_007 --threads $t
#results in 3_msa.fasta in each cluster

#step 5 Partitioning reads
trycycler partition --reads reads.fastq --cluster_dirs clusters/cluster_* --threads $t
#results in 4_reads.fasta in each cluster, containing its share of reads

#step 6 Generating consensus
#uses the 3 files from the previous 3 steps to generate consensus fasta for each cluster
trycycler consensus --cluster_dir clusters/cluster_001 --threads $t --verbose
#trycycler consensus --cluster_dir clusters/cluster_007 --threads $t --verbose
#results in a consensus fasta for each cluster, which can then be concatenated into a single fasta
cat trycycler/cluster_*/7_final_consensus.fasta > trycycler/consensus.fasta
#activates virtual environment for medaka since it couldn't be added to conda environment due to conflicting packages
cd ~/medaka
. ./venv/bin/activate
cd ~/Trycycler/Run3
#optional: polishing step for each consensus
for c in clusters/cluster_*; do
    medaka_consensus -i "$c"/4_reads.fastq -d "$c"/7_final_consensus.fasta -o "$c"/medaka -m r941_min_sup_g507 -t $t
    mv "$c"/medaka/consensus.fasta "$c"/8_medaka.fasta
    rm -r "$c"/medaka "$c"/*.fai "$c"/*.mmi  # clean up
done

