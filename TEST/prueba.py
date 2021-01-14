import sys
sys.path.append('.')

from DNA_RNA_Protein_Module import DNA, RNA, Protein





"""
#FIND Functions
def findBeginSequenceOnRNA(rnaSequence):
    return findInString('AUG', rnaSequence)

def findBeginSequenceOnDNA(dnaSequence):
    return findInString('ATG', dnaSequence)

def findEndSequenceOnRNA(rnaSequence):
    return sorted(findInString('UAA', rnaSequence) + findInString('UAG', rnaSequence) + findInString('UGA', rnaSequence))

def findEndSequenceOnDNA(dnaSequence):
    return sorted(findInString('TAA', dnaSequence) + findInString('TAG', dnaSequence) + findInString('TGA', dnaSequence))
"""



"""
def isSequenceDNA(seq):
    return genericSequenceController(seq, ["A","T","C","G"])

def isSequenceRNA(seq):
    return genericSequenceController(seq, ["A","U","C","G"])

def isSequenceProtein(seq):
    return genericSequenceController(seq, ["I","M","T","N","K","S","R","L","P","H","Q","V","A","D","E","G","F","Y","C","W"])
"""
"""
def createRNAbyDNA(dnaSequence):
    return dnaSequence.replace("T","U")

def createDNAbyRNA(rnaSequence):
    return rnaSequence.replace("U","T")

def translateARNtoProtein(seq):
    table = { 
        'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M', 
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T', 
        'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K', 
        'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R', 
        'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L', 
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P', 
        'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q', 
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R', 
        'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V', 
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A', 
        'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E', 
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G', 
        'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S', 
        'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L', 
        'UAC':'Y', 'UAU':'Y', 'UAA':'_', 'UAG':'_', 
        'UGC':'C', 'UGU':'C', 'UGA':'_', 'UGG':'W',
    } 
    protein ="" 

    for i in range(0, len(seq), 3): 
        codon = seq[i:i + 3] 
        try:
            protein+= table[codon]
        except :
            pass
    return protein 
"""