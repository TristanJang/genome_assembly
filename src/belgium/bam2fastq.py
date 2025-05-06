import subprocess
import os
grouphome = os.environ['GROUPHOME']
f = open("isolates.txt", "r")
d ={}
for i in f:
    i = i.strip()
    value = i[-6:]
    d[i] = value
new = open("isolates2.txt","w")
for i in d:
    new.write(d[i]+ "\n")
#print(d)
#for i in d:
    #input = "samtools bam2fq bam_files/"+i+".bam > "+d[i]+".fastq"
    #print(input)
    #subprocess.call(input, shell=True)
