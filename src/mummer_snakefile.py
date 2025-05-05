import os
grouphome = os.environ['GROUPHOME']
ISOLATES = [i for i in open('/grp/valafar/data/depot/assembly/south_africa/isolates.txt').read().split('\n') if len(i) > 0]

rule All:
    input:
        expand(grouphome + "/data/depot/depot/assembly/south_africa/{isolate}/mummer/{isolate}.report", isolate = ISOLATES),
        expand(grouphome + "/data/depot/depot/assembly/south_africa/{isolate}/mummer/{isolate}.delta", isolate = ISOLATES),
        expand(grouphome + "/data/depot/depot/assembly/south_africa/{isolate}/mummer/{isolate}.1delta", isolate = ISOLATES),
        expand(grouphome + "/data/depot/depot/assembly/south_africa/{isolate}/mummer/{isolate}.mdelta", isolate = ISOLATES),
        expand(grouphome + "/data/depot/depot/assembly/south_africa/{isolate}/mummer/{isolate}.1coords", isolate = ISOLATES),
        expand(grouphome + "/data/depot/depot/assembly/south_africa/{isolate}/mummer/{isolate}.mcoords", isolate = ISOLATES),
        expand(grouphome + "/data/depot/depot/assembly/south_africa/{isolate}/mummer/{isolate}.snps", isolate = ISOLATES),
        expand(grouphome + "/data/depot/depot/assembly/south_africa/{isolate}/mummer/{isolate}.rdiff", isolate = ISOLATES),
        expand(grouphome + "/data/depot/depot/assembly/south_africa/{isolate}/mummer/{isolate}.qdiff", isolate = ISOLATES)

#dnadiff for each isolate:
rule mummer:
    input:
        grouphome + "/data/depot/assembly/south_africa/{isolate}/assembly/circ/06.fixstart.fasta"
    output:
        grouphome + "/data/depot/depot/assembly/south_africa/{isolate}/mummer/{isolate}.report",
        grouphome + "/data/depot/depot/assembly/south_africa/{isolate}/mummer/{isolate}.delta",
        grouphome + "/data/depot/depot/assembly/south_africa/{isolate}/mummer/{isolate}.1delta",
        grouphome + "/data/depot/depot/assembly/south_africa/{isolate}/mummer/{isolate}.mdelta",
        grouphome + "/data/depot/depot/assembly/south_africa/{isolate}/mummer/{isolate}.1coords",
        grouphome + "/data/depot/depot/assembly/south_africa/{isolate}/mummer/{isolate}.mcoords",
        grouphome + "/data/depot/depot/assembly/south_africa/{isolate}/mummer/{isolate}.snps",
        grouphome + "/data/depot/depot/assembly/south_africa/{isolate}/mummer/{isolate}.rdiff",
        grouphome + "/data/depot/depot/assembly/south_africa/{isolate}/mummer/{isolate}.qdiff"
    params:
        isolate = ISOLATES
    shell:
       """dnadiff /grp/valafar/data/genomes/H37Rv-NCBI.fasta {input} -p {wildcards.isolate}"""
       #"""mkdir {wildcards.isolate}/mummer"""
       #"""mv {wildcards.isolate}.* {wildcards.isolate}/mummer/"""