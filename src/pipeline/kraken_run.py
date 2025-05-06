import os

islist = os.listdir("/home/nthosar9846/assembly/hifi/B09_R31038_BSL_New/")
isol = []
for i in islist:
    isol.append(i.split('.')[0])

isolates = list(set(isol))
isolates.remove('assembly')
for i in isolates:
    os.system(
        "/grp/valafar/data/depot/nanopore_assembly/maryam/tools/kraken2/kraken_unzipped/kraken2 --db /grp/valafar/data/depot/nanopore_assembly/contamination_db/ /home/nthosar9846/assembly/hifi/B09_R31038_BSL_New/"+i+".fasta --use-names --report /home/nthosar9846/assembly/hifi/B09_R31038_BSL_New/"+i+"_class_report.kraken > /home/nthosar9846/assembly/hifi/B09_R31038_BSL_New/"+i+"_contig_classification.kraken")


