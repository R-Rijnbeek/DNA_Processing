# -*- coding: utf-8 -*-
"""
test module for dna_processing: Test dodule to test the DNA_ProcessPackage
"""

# ======== IMPORTS ===========

from dna_processing import DNA, RNA, Protein, loadFile, findProteinsequences

# ======== TEST FUNCTIONS =======

def test_1():
    dnaString = loadFile("DATA\\DNA\\DNA_seq_altered.txt")
    dna = DNA(dnaString)
    rna = dna.createRNA()
    dna1 = rna.createDNA()
    if (dna.getSequence() == dna1.getSequence()):
        print("TEST 1: SUCCESS")
        return True
    return False

def test_2():
    dnaString_1 = loadFile("DATA\\DNA\\DNA_seq_altered.txt")
    dna = DNA(dnaString_1)
    dna.writeToFile("DATA\\DNA\\DNA_test_2.txt")
    dnaString_2 = loadFile("DATA\\DNA\\DNA_test_2.txt")
    if (dnaString_1 == dnaString_2):
        print("TEST 2: SUCCESS")
        return True
    return False

def test_3():
    dnaString = loadFile("DATA\\DNA\\DNA_seq_altered.txt")
    dna = DNA(dnaString)
    rna = dna.createRNA()
    rna.writeToFile("DATA\\RNA\\RNA_test_3.txt")
    rnaString = loadFile("DATA\\RNA\\RNA_test_3.txt")
    if ( (rna.getSequence() == rnaString) and (dna.getSequence() == dnaString) ):
        print("TEST 3: SUCCESS")
        return True
    return False

def test_4():
    dnaString = loadFile("DATA\\DNA\\DNA_test_2.txt")
    dna = DNA(dnaString)
    rnaString = loadFile("DATA\\RNA\\RNA_test_3.txt")
    rna = RNA(rnaString)
    rna_beginPositions = rna.findBeginSequence()
    rna_endPositions = rna.findEndSequence()
    dna_beginPositions = dna.findBeginSequence()
    dna_endPositions = dna.findEndSequence()
    if ((rna_beginPositions == dna_beginPositions) and (rna_endPositions == dna_endPositions)):
        valid_sequences = findProteinsequences(rna_beginPositions,rna_endPositions)
        firstInterval = valid_sequences[0]
        rna_subsection = rna.getSubSection(firstInterval)
        protein = rna_subsection.createProtein()
        protein.writeToFile("DATA\\PROTEIN\\Protein_test4.txt")
        builded_protein = loadFile("DATA\\PROTEIN\\Protein_test4.txt")
        valid_protein = loadFile("DATA\\PROTEIN\\amino_acid_sequence_original.txt")
        if ((protein.getSequence() == valid_protein) and (builded_protein == valid_protein)):
            print("TEST 4: SUCCESS")
            return True
    return False

def testProcess():
    """
    """
    try:
        if (test_1()):
            if (test_2()):
                if (test_3()):
                    if test_4():
                        print("TESTS SUCCESSFULL PASSED")
                        return True
        return False
    except Exception as exc:
        print(f'ERROR: {exc}')
        return False

# ======== EXECUTE TESTS ==========

if __name__ == "__main__":
    
    testProcess()