def get_sequences(file_dir):
    sequences = []
    with open(file_dir, 'r') as f:
        sequence = ''
        for line in f:
            if line.startswith('>'):
                if sequence:
                    sequences.append(sequence)
                    sequence = ''
            else:
                sequence += line.strip()
        sequences.append(sequence)
    return sequences

def longest_common_substring(sequences):
    if not sequences:
        return ''

    
    reference = sequences[0]
    longest_substr = ''
    max_length = 0

    for i in range(len(reference)):
        for j in range(i + 1, len(reference) + 1):
            substring = reference[i:j]
            if all(substring in seq for seq in sequences[1:]) and len(substring) > max_length:
                max_length = len(substring)
                longest_substr = substring
    return longest_substr

file_dir = '/Users/idean/Downloads/rosalind_lcsm.txt'
sequences = get_sequences(file_dir)
result = longest_common_substring(sequences)
print(result)
