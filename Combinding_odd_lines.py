def combinding_sentense(file_dir) : 
    sentenses = []
    count = 0
    with open(file_dir, 'r') as f : 
        for line in f : 
            if count % 2 != 0 : 
                line = line.strip()
                sentenses.append(line)
            count += 1
            
    return sentenses

file_dir = '/Users/idean/Downloads/rosalind_ini5.txt'
sentenses = combinding_sentense(file_dir)

for i in sentenses :
    print(i)
