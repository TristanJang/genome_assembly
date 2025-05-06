import pandas as pd
import subprocess
import os
grouphome = os.environ['GROUPHOME']
df = pd.read_csv("hifi_reads_barcode_names.txt", header=None, index_col=0, squeeze = True)
d = df.to_dict()
for i in d:
    input1 = "cp " + grouphome + "/data/depot/temp/r84100_20230718_182455/1_B01/hifi_reads/"+ i + ".bam "+grouphome+"/data/depot/assembly/south_africa/"+d[i]+".bam"
    input2 = "samtools bam2fq "+grouphome+"/data/depot/assembly/south_africa/"+d[i]+".bam > "+grouphome+"/data/depot/assembly/south_africa/"+d[i]+".fastq"
    subprocess.call(input1, shell=True)
    subprocess.call(input2, shell=True)
