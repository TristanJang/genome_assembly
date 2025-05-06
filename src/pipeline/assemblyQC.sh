#!/bin/bash
eval "$(conda shell.bash hook)"
conda activate varscan
set -x
for isolate_dir in $(cat /grp/valafar/data/depot/assembly/south_africa/list_of_iso_dirs.txt)
do
isolate=$(echo $isolate_dir | grep -o "[^/]\+$" | cut -d. -f1)
python /home/nthosar9846/Pycharm/assemblyQC.py -g $isolate_dir -r /grp/valafar/data/depot/assembly/south_africa/$isolate/${isolate}_filtered_reads.fastq
done
