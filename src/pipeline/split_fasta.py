from Bio import SeqIO
input_path = input("Enter a multifasta file to split: ")
outpath= input("Enter the path where you want the output to be :")
multifa=list(SeqIO.parse(input_path, "fasta"))
contigs={}
for contig in multifa:
     contigs[contig.id]=str(contig.seq)

for cons in contigs:
     with open(outpath+cons+".fasta",'w') as f:
             f.write(">"+cons+"\n")
             f.write(contigs[cons])

