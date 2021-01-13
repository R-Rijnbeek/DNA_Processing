def loadDNAFile(path):
    return open( path, "r").read().replace("\n", "").replace("\r", "") 

dnaString = loadDNAFile("DATA\DNA\DNA_seq_altered.txt")

print(dnaString)


    


