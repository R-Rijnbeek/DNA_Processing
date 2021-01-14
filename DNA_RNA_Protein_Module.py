import re
from pathlib import Path

def findInString(val, seq):
    return [m.start() for m in re.finditer(f'(?={val})', seq)]

def loadFile(path):
    return open( path, "r").read().replace("\n", "").replace("\r", "")

def isSequenceMultipleOfThree(seq):
    return len(seq)%3 == 0

def writeToFile(string ,path):
    if Path(path).parent.is_dir():
        f = open(path, "w")
        f.write(string)
        f.close()
        return True
    else:
        print("Directory do not exists")
        return False

def getSubSectionOfSequence(seq,interval):
    try:
        return seq[interval[0]:interval[1]]
    except Exception as exc:
        print(f'ERROR: {exc}')
        return None

# controllers

def genericSequenceController(seq, valuesToMatch):
    removeDuplicates =  "".join(set(seq))
    for char in removeDuplicates:
        if char not in valuesToMatch:
            return False
    return True

#protein detector

def filterListByGreatherThanValue(value, sequence):
    return list(filter((value).__le__, sequence))


def findProteinsequences(beqinPositions, endPositions):
    sequence_list = []
    reducedEndPositions = endPositions
    for begin in beqinPositions:
        reducedEndPositions = filterListByGreatherThanValue(begin,reducedEndPositions)
        for end in reducedEndPositions:
            if ((begin-end)%3==0):
                sequence_list.append([begin,end])
                break
    return sequence_list

class DNA():
    def __init__(self, seq):
        self.value = None
        if (self.isSequenceDNA(seq)):
            self.value = seq

    def isSequenceDNA(self, seq):
        return genericSequenceController(seq, ["A","T","C","G"])

    def getSequence(self):
        return self.value

    def getSubSection(self,interval):
        return DNA(getSubSectionOfSequence(self.value, interval))

    def createRNA(self):
        return RNA(self.value.replace("T","U"))

    def findBeginSequence(self):
        return findInString('ATG', self.value)

    def findEndSequence(self):
        return sorted(findInString('TAA', self.value) + findInString('TAG', self.value) + findInString('TGA', self.value))

    def isSequenceMultipleOfThree(self):
        return isSequenceMultipleOfThree(self.value)
    
    def writeToFile(self,path):
        return writeToFile(self.value,path)


class RNA():
    def __init__(self, seq):
        self.value = None
        if (self.isSequenceRNA(seq)):
            self.value = seq

    def isSequenceRNA(self, seq):
        return genericSequenceController(seq, ["A","U","C","G"])

    def getSequence(self):
        return self.value

    def getSubSection(self,interval):
        return RNA(getSubSectionOfSequence(self.value, interval))

    def createDNA(self):
        return DNA(self.value.replace("U","T"))

    def createProtein(self):
        table = { 
            'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T', 
            'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R', 
            'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P', 
            'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R', 
            'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A', 
            'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G', 
            'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S', 'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L', 
            'UAC':'Y', 'UAU':'Y', 'UAA':'_', 'UAG':'_', 'UGC':'C', 'UGU':'C', 'UGA':'_', 'UGG':'W',
        } 
        protein ="" 

        for i in range(0, len(self.value), 3): 
            codon = self.value[i:i + 3] 
            try:
                protein+= table[codon]
            except :
                pass
        return Protein(protein)

    def findBeginSequence(self):
        return findInString('AUG', self.value)

    def findEndSequence(self):
        return sorted(findInString('UAA', self.value) + findInString('UAG', self.value) + findInString('UGA', self.value))

    def isSequenceMultipleOfThree(self):
        return isSequenceMultipleOfThree(self.value)
    
    def writeToFile(self,path):
        return writeToFile(self.value,path)


class Protein():
    def __init__(self, seq):
        self.value = None
        if (self.isSequenceProtein(seq)):
            self.value = seq

    def getSequence(self):
        return self.value

    def getSubSection(self,interval):
        return Protein(getSubSectionOfSequence(self.value, interval))

    def isSequenceProtein(self,seq):
        return genericSequenceController(seq, ["I","M","T","N","K","S","R","L","P","H","Q","V","A","D","E","G","F","Y","C","W"])

    def writeToFile(self,path):
        return writeToFile(self.value,path)



if __name__ == "__main__":

    dnaString = loadFile("DATA\\DNA\\DNA_seq_altered.txt")

    dna = DNA(dnaString)
    rna = dna.createRNA()
    dna1 = rna.createDNA()

    print(dna.value==dna1.value)

    protein = rna.createProtein()

    print(protein)
    """
    print(dnaString)
    print(isDNAComplete(dnaString))
    print(isSequenceDNA(dnaString))
    rna = createRNAbyDNA(dnaString)
    begin = findBeginSequenceOnRNA(rna)
    end = findEndSequenceOnRNA(rna)
    print(translateARNtoProtein(rna[20:935]))

    #print(filterListByGreatherThanValue(5,[14,7,6,5,3,2]))
    sequence_List = findProteinsequences(begin, end)
    print(translateARNtoProtein(rna[sequence_List[0][0]:(sequence_List[0][1]+3)]))
    """


    


