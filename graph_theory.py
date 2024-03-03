#Brief introduction to graph theory
def parse_fasta(fasta):
    sequences = []
    current_sequence = ""
    for line in fasta:
        if line.startswith(">"):
            if current_sequence:
                sequences.append((header, current_sequence))
            header = line.strip()[1:]
            current_sequence = ""
        else:
            current_sequence += line.strip()
    if current_sequence:
        sequences.append((header, current_sequence))
    return sequences

def overlap_graph(sequences, k):
    adjacency_list = []

    for i in range(len(sequences)):
        for j in range(len(sequences)):
            if i != j and sequences[i][1][-k:] == sequences[j][1][:k]:
                adjacency_list.append((sequences[i][0], sequences[j][0]))

    return adjacency_list

# Read input from a file (replace 'input.fasta' with your input file)
input_dir = '/Users/idean/Downloads/rosalind_grph (1).txt'
with open(input_dir, 'r') as file:
    fasta_lines = file.readlines()

# Parse FASTA format
sequences = parse_fasta(fasta_lines)

# Generate overlap graph for k=3
k_value = 3
overlap_edges = overlap_graph(sequences, k_value)

tmp_list = []

# Print the adjacency list in the specified format
for edge in overlap_edges:
    print(edge[0], edge[1])
