import subprocess

file = open("isolates2.txt","r")

for isolate in file:
    isolate = isolate.strip()
    command1 = "circlator fixstart "+ isolate+ "/assembly/assembly.fasta " + isolate + " --genes_fa ../../../../resources/dnaA.fasta"
    command2 = "mkdir " + isolate+"/circ"
    command3 = "mv " + isolate + ".* " + isolate +"/circ/"
    print(command1)
    print(command2)
    print(command3)
    subprocess.call(command1 , shell=True)
    subprocess.call(command2 , shell=True)
    subprocess.call(command3 , shell=True)