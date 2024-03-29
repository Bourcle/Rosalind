#DNA complementary
sampledata = 'GAACGCGTGTTATATTCTGTCTGGTACAACTCTACAGTTTCCAATCTGAGCTGCAGATCGCCCAACCGCCCTCAACCCTGCTGAGCCTTCGCGGAGGGAACTAATTCCCCCTTCGCCCGGATATACCTCGGGTAGGGCCAGTCGTTTGGACCACCTGGTGTGAAGCACAACTTTTATACCCTACGGACAGCACGCTATGGTTCGAGCGCGGATAATTCGCTTCGGGACTTAGTGCACTGCTCACTTGTGCGGCGAAGTATTCGCCTCAAGCCACCGGCTATCACGTTTAGCGACGGTGAACCTTCGAATCCCGTGGCGTGGGTCCCCTTCGTAACCAAGTGACATTGAAGCAGATAGACCAACTTTGTAAACTGCGAGCCAAGTTATTGCGAGCGCCCGACGAGGCCGCACGTCTGCTGATATGCGCGAGACAGACGTACCACTACCACCGCAAGATGACGGATTAGTGATATCCTATGAGTGGTTAGTGCTAGCCATGGTGAACCGGTGCCCACGGGAATCCCGTATTTGGGTAACAACTGTTATAGGTTGGAGTCGAACACCCGCTCAAACAACCGACGGAATCCGTCGGACAGCTGAATGGCACAGTGCATTAGTATGGAATCTATTACACTCGACCGGTATAATACACGCAGTCACACAATCTGTTACATTGTGTAATGGGAGTCAATTAGGAGGAAGGCCGCACCATGTACGTGATAGTCTCAACGAGTGTTAAAGCAGATATTTTATGTGTCCCCGAAAGCAAAGCATCTTTTTAACCTATAATCTTAAAGATCTCGTCGGGGTACATGACTTGCTCTTTTCGTGTTGATCTGACCCGATAAGAGGCTCAGGTCGGTTTATGCCGCTCGCTAAGTAGGATCACTCTGTGATAACAAATTTCATAATTTGCGCGATCTCCACGCGGACCGCAGAAGAGACATAAATAGCTAAATTTTTCCGGAAAGGCTGGC'
list_data = list(sampledata)

def compliments(code) : 
    if code == 'A' : 
        rev = 'T'
    elif code == 'C' : 
        rev = 'G'
    elif code == 'G' : 
        rev = 'C'
    else : rev = 'A'
    
    return rev

lists = []
for i in list_data : 
    lists.append(compliments(i))
lists.reverse()
answer = ''.join(lists)
print(answer)    
