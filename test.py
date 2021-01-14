import re

def findInString(val, seq):
    return [m.start() for m in re.finditer(f'(?={val})', seq)]

def loadDNAFile(path):
    return open( path, "r").read().replace("\n", "").replace("\r", "")

def isDNAComplete(dnaSequence):
    return len(dnaSequence)%3 == 0

#FIND Functions
def findBeginSequenceOnRNA(rnaSequence):
    return findInString('AUG', rnaSequence)

def findBeginSequenceOnDNA(dnaSequence):
    return findInString('ATG', dnaSequence)

def findEndSequenceOnRNA(rnaSequence):
    return findInString('UAA', rnaSequence) + findInString('UAG', rnaSequence) + findInString('UGA', rnaSequence)

def findEndSequenceOnDNA(dnaSequence):
    return findInString('TAA', dnaSequence) + findInString('TAG', dnaSequence) + findInString('TGA', dnaSequence)

# DNA controller
def idSequenceDNA(seq):
    removeDuplicates =  "".join(set(seq))
    for char in removeDuplicates:
        if char not in ["A","T","C","G"]:
            return False
    return True

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



if __name__ == "__main__":

    dnaString = loadDNAFile("DATA\\DNA\\DNA_seq_altered.txt")

    print(dnaString)
    print(isDNAComplete(dnaString))
    print(idSequenceDNA(dnaString))
    rna = createRNAbyDNA(dnaString)
    print(findBeginSequenceOnRNA(rna))
    print(findEndSequenceOnRNA(rna))
    print(translateARNtoProtein(rna[20:935]))

    print(findInString("st", "st st    stst"))


    


